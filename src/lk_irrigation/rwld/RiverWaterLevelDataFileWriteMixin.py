import os
from dataclasses import asdict

from utils import JSONFile, Log, Time, TimeFormat

log = Log("RiverWaterLevelDataFileWriteMixin")


class RiverWaterLevelDataFileWriteMixin:
    URL_STRUCTURED = (
        "https://raw.githubusercontent.com"
        + "/nuuuwan/lk_irrigation/refs/heads/main/data/alert_data.json"
    )

    def write(self):
        if self.json_file.exists:
            return False
        os.makedirs(self.dir_path, exist_ok=True)
        self.json_file.write(asdict(self))
        log.info(f"Wrote {self.json_file}")
        return True

    @classmethod
    def write_alert_data(cls, d_list):
        json_file = JSONFile(os.path.join(cls.DIR_DATA, "alert_data.json"))

        data = {}
        data["url_source"] = cls.REMOTE_URL
        data["url_structured"] = cls.URL_STRUCTURED
        data["event_measure"] = "river_water_level_m"

        event_data = {}
        for d in d_list:
            ent_id = d["station_name"]
            time_id = TimeFormat.TIME_ID.format(Time(d["time_ut"]))
            date_part = time_id[:8]
            time_part = time_id[9:]
            water_level_m = round(d["water_level_m"], 3)

            if ent_id not in event_data:
                event_data[ent_id] = {}
            if date_part not in event_data[ent_id]:
                event_data[ent_id][date_part] = {}
            event_data[ent_id][date_part][time_part] = water_level_m

        data["event_data"] = event_data
        json_file.write(data)
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

        # alert_data
        cls.write_alert_data(d_list)
