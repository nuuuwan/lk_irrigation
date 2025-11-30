import os
from dataclasses import asdict, dataclass
from functools import cached_property

import requests
from utils import JSONFile, Log

from lk_irrigation.base.HasTimeMixin import HasTimeMixin
from lk_irrigation.core.Station import Station

log = Log("RiverWaterLevelData")


@dataclass
class RiverWaterLevelData(HasTimeMixin):

    DIR_DATA_RWLD = os.path.join("data", "rwlds")
    REMOTE_URL = (
        "https://services3.arcgis.com"
        + "/J7ZFXmR8rSmQ3FGf/arcgis/rest/services"
        + "/gauges_2_view/FeatureServer/0/query"
    )

    station_name: str
    time_ut: int
    water_level_m: float

    @cached_property
    def station(self):
        return Station.from_name(self.station_name)

    @cached_property
    def dir_path(self) -> str:
        return os.path.join(
            self.DIR_DATA_RWLD,
            f"{self.station.river.basin.file_prefix}-basin",
            f"{self.station.river.file_prefix}-river",
            f"{self.station.file_prefix}-station",
            self.part_dir_time,
        )

    @cached_property
    def json_path(self) -> str:
        return os.path.join(self.dir_path, f"{self.time_str}.json")

    @cached_property
    def json_file(self) -> JSONFile:
        return JSONFile(self.json_path)

    def write(self):
        os.makedirs(self.dir_path, exist_ok=True)
        self.json_file.write(asdict(self))
        log.info(f"Wrote {self.json_file}")

    def validate_remote(self, d):
        converstion_factor = 1.0
        if self.station.water_level_unit == "ft":
            converstion_factor = 0.3048
        for [expected, actual, label] in [
            [self.station.river.basin.name, d["basin"], "basin"],
            [
                self.station.alert_level,
                d["alertpull"] * converstion_factor,
                "alert_level",
            ],
            [
                self.station.minor_flood_level_m,
                d["minorpull"] * converstion_factor,
                "minor_flood_level_m",
            ],
            [
                self.station.major_flood_level_m,
                d["majorpull"] * converstion_factor,
                "major_flood_level_m",
            ],
        ]:
            assert (
                expected == actual
            ), f"[validate {label}]: {expected} != {actual}"

    @classmethod
    def from_remote_data_dict(cls, d: dict) -> "RiverWaterLevelData":
        rwld = cls(
            station_name=d["gauge"],
            time_ut=int(d["EditDate"]) // 1000,
            water_level_m=float(d["water_level"]),
        )
        rwld.validate_remote(d)

        if rwld.station.water_level_unit == "ft":
            rwld.water_level_m *= 0.3048

        return rwld

    @classmethod
    def __load_data_list_from_remote_page__(
        cls,
        station_name: str,
        days_offset: int,
        page_offset: int,
        page_size: int,
    ):

        params = {
            "resultOffset": page_offset,
            "resultRecordCount": page_size,
            "where": "((CreationDate BETWEEN CURRENT_TIMESTAMP"
            + f" - {days_offset} AND CURRENT_TIMESTAMP))"
            + f" AND (gauge='{station_name}')",
            "f": "json",
            "orderByFields": "CreationDate DESC",
            "outFields": "*",
            "resultType": "standard",
            "returnGeometry": "false",
            "spatialRel": "esriSpatialRelIntersects",
        }
        try:
            r = requests.get(cls.REMOTE_URL, params=params, timeout=10)
            d_list = [q["attributes"] for q in r.json().get("features", [])]
            log.debug(f"Fetched {len(d_list)} for {station_name}")
            return d_list
        except Exception as e:
            log.error(f"Error fetching data for {station_name}: {e}")
            return None

    @classmethod
    def __load_data_list_from_remote__(
        cls,
        station_name: str,
        days_offset: int,
        total_pages: int,
        page_size: int,
    ):
        assert (
            total_pages % page_size == 0
        ), "total_pages must be a multiple of page_size"
        assert Station.from_name(
            station_name
        ), f"Station not found: {station_name}"

        d_list = []
        for page_offset in range(0, total_pages + page_size, page_size):
            d_list_for_page = cls.__load_data_list_from_remote_page__(
                station_name, days_offset, page_offset, page_size
            )
            if d_list_for_page is not None:
                d_list += d_list_for_page

        log.debug(f"Fetched {len(d_list)} for {station_name}")
        return d_list

    @classmethod
    def load_station_from_remote(
        cls,
        station_name: str,
        days_offset: int,
        total_pages: int,
        page_size: int,
    ):
        rwld_list = [
            cls.from_remote_data_dict(d)
            for d in cls.__load_data_list_from_remote__(
                station_name, days_offset, total_pages, page_size
            )
        ]
        for rwld in rwld_list:
            rwld.write()
        log.info(
            f"Loaded {len(rwld_list)} RWLD entries"
            + f" from remote for {station_name}"
        )
        return rwld_list

    @classmethod
    def load_all_from_remote(
        cls,
        days_offset: int,
        total_pages: int,
        page_size: int,
    ):
        rwld_list = []
        for station in Station.list_all():
            rwld_list += cls.load_station_from_remote(
                station.name, days_offset, total_pages, page_size
            )
        log.info(f"Loaded total {len(rwld_list)} RWLD entries from remote")
        return rwld_list
