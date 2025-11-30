import os
from dataclasses import asdict

from utils import JSONFile, Log, TSVFile

log = Log("RiverWaterLevelDataFileWriteMixin")


class RiverWaterLevelDataFileWriteMixin:

    def write(self):
        if self.json_file.exists:
            return
        os.makedirs(self.dir_path, exist_ok=True)
        self.json_file.write(asdict(self))
        log.info(f"Wrote {self.json_file}")

    @classmethod
    def write_all(cls):
        d_list = [asdict(q) for q in cls.list_all()]
        for n in [100, 1000, None]:
            d_list_custom = d_list[:n] if n else d_list
            file_name = f"latest-{n}" if n else "all"

            tsv_file_path = os.path.join("data", f"{file_name}.tsv")
            tsv_file = TSVFile(tsv_file_path)
            tsv_file.write(d_list_custom)
            log.info(f"Wrote {tsv_file}")

            json_file_path = os.path.join("data", f"{file_name}.json")
            if n is None:
                assert cls.ALL_PATH == json_file_path
            json_file = JSONFile(json_file_path)
            json_file.write(d_list_custom)
            log.info(f"Wrote {json_file}")
