import os
from dataclasses import asdict
from functools import cache, cached_property

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

    @classmethod
    def __gen_all_json_files__(cls) -> list[JSONFile]:
        for root, _, files in os.walk(cls.DIR_DATA_RWLD):
            for file in files:
                if file.endswith(".json"):
                    yield JSONFile(os.path.join(root, file))

    @classmethod
    def __gen_all_ds__(cls):
        for json_file in cls.__gen_all_json_files__():
            data = json_file.read()
            yield data

    @classmethod
    def __gen_all__(cls):
        for data in cls.__gen_all_ds__():
            yield cls(**data)

    @classmethod
    @cache
    def list_all(cls) -> list:
        d_list = list(cls.__gen_all__())
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
