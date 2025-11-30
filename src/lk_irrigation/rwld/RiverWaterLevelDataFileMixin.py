import os
from dataclasses import asdict
from functools import cached_property

from utils import JSONFile, Log

log = Log("RiverWaterLevelDataFileMixin")


class RiverWaterLevelDataFileMixin:
    DIR_DATA_RWLD = os.path.join("data", "rwlds")

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
        if self.json_file.exists:
            return
        os.makedirs(self.dir_path, exist_ok=True)
        self.json_file.write(asdict(self))
        log.info(f"Wrote {self.json_file}")
