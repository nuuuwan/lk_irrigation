import os
from dataclasses import asdict

from utils import JSONFile, Log, TSVFile

log = Log("RiverWaterLevelDataFileWriteMixin")


class RiverWaterLevelDataFileWriteMixin:
    URL_STRUCTURED = (
        "https://raw.githubusercontent.com"
        + "/nuuuwan/lk_irrigation/refs/heads/main/data/all.json"
    )

    def write(self):
        if self.json_file.exists:
            return False
        os.makedirs(self.dir_path, exist_ok=True)
        self.json_file.write(asdict(self))
        log.info(f"Wrote {self.json_file}")
        return True

    @classmethod
    def write_alert_data_list(cls, d_list):
        json_file = JSONFile(
            os.path.join(cls.DIR_DATA, "alert_data_list.json")
        )

        def mapper(d):
            return {
                "id": d["station_name"],
                "time_ut": d["time_ut"],
                "value_idx": {
                    "water_level_m": d["water_level_m"],
                },
                "url_source": cls.REMOTE_URL,
                "url_structured": cls.URL_STRUCTURED,
            }

        alert_data_list = [mapper(d) for d in d_list]
        json_file.write(alert_data_list)
        log.info(f"Wrote {json_file}")

    @classmethod
    def write_all(cls):
        d_list = [asdict(q) for q in cls.list_all_from_files()]
        d_list.reverse()

        json_file = JSONFile(cls.ALL_PATH)
        json_file.write(d_list)
        log.info(f"Wrote {json_file}")

        cls.list_all.cache_clear()
        cls.station_to_list.cache_clear()
        cls.station_to_latest.cache_clear()
        cls.station_to_ror.cache_clear()
        log.debug("Cleared caches for list_all and related methods.")

        # alert_data_list
        cls.write_alert_data_list(d_list)
