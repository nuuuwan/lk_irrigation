import os
from functools import cache, cached_property

from utils import JSONFile, Log

log = Log("RiverWaterLevelDataFileReadOnlyMixin")


class RiverWaterLevelDataFileReadOnlyMixin:
    DIR_DATA = "data"
    DIR_DATA_RWLD = os.path.join(DIR_DATA, "rwlds")
    ALL_PATH = os.path.join(DIR_DATA, "all.json")

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

    @classmethod
    @cache
    def list_all(cls) -> list:
        raw_d_list = JSONFile(cls.ALL_PATH).read()
        d_list = [cls(**d) for d in raw_d_list]
        d_list.sort(
            key=lambda d: (
                -d.time_ut,
                d.station.river.basin.name,
                d.station.river.name,
                d.station.name,
            )
        )
        log.debug(f"Loaded {len(d_list)} RWLDs.")
        return d_list

    @classmethod
    @cache
    def station_to_list(cls) -> dict[str, list]:
        d_list = cls.list_all()
        idx = {}
        for d in d_list:
            if d.station_name not in idx:
                idx[d.station_name] = []
            idx[d.station_name].append(d)
        return idx
