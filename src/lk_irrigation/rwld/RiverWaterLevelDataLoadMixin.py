import time

import requests
from utils import Log

from lk_irrigation.core.Station import Station

log = Log("RiverWaterLevelDataLoadMixin")


class RiverWaterLevelDataLoadMixin:
    REMOTE_URL = (
        "https://services3.arcgis.com"
        + "/J7ZFXmR8rSmQ3FGf/arcgis/rest/services"
        + "/gauges_2_view/FeatureServer/0/query"
    )

    def validate_remote(self, d):
        converstion_factor = 1.0
        if self.station.water_level_unit == "ft":
            converstion_factor = 0.3048
        for [expected, actual, label] in [
            [self.station.river.basin.name, d["basin"], "basin"],
            [
                self.station.alert_level_m,
                d["alertpull"] * converstion_factor,
                "alert_level_m",
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
    def from_remote_data_dict(cls, d: dict):
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

        max_t_timeout = 30
        timeout_mult = 2
        t_timeout = 1
        time.sleep(t_timeout)
        while True:
            try:
                response = requests.get(
                    cls.REMOTE_URL, params=params, timeout=max_t_timeout
                )
                d_list = [
                    q["attributes"]
                    for q in response.json().get("features", [])
                ]
                return d_list
            except Exception as e:
                log.error(f"Error fetching data for {station_name}: {e}")
                t_timeout *= timeout_mult
                if t_timeout > max_t_timeout:
                    log.error(f"Data fetch from {station_name} failed.")
                    return None
                log.debug(f"Sleeping {t_timeout}s, before Retrying...")
                time.sleep(t_timeout)

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
        for page_offset in range(0, total_pages, page_size):
            d_list_for_page = cls.__load_data_list_from_remote_page__(
                station_name, days_offset, page_offset, page_size
            )
            if d_list_for_page is None or len(d_list_for_page) == 0:
                break
            d_list += d_list_for_page
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
