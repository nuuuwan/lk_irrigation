from utils import File, Format, Log, Time, TimeFormat

from lk_irrigation.base import Markdown
from lk_irrigation.charts.ChartMap import ChartMap
from lk_irrigation.rwld.RiverWaterLevelData import RiverWaterLevelData

log = Log("ReadMe")


class ReadMe:
    PATH = "README.md"
    URL_IRRIGATION = "https://www.irrigation.gov.lk"
    URL_HYDROLOGY = (
        URL_IRRIGATION
        + "/web/index.php"
        + "?option=com_content&view=article&id=27&Itemid=128&lang=en"
    )
    URL_ARCGIS_DASHBOARD = (
        "https://www.arcgis.com"
        + "/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38"
    )
    URL_LOADER = "src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py"
    URL_DATA = RiverWaterLevelData.DIR_DATA_RWLD

    def __init__(self):
        self.rwld_list = RiverWaterLevelData.list_all()
        self.station_to_rwld_list = RiverWaterLevelData.station_to_list()

    def get_lines_header(self) -> list[str]:
        max_time_ut = max([rwld.time_ut for rwld in self.rwld_list])
        time_str = TimeFormat.TIME.format(Time(max_time_ut))
        time_updated_for_badge = Format.badge(time_str)
        return [
            "# lk_irrigation 🇱🇰",
            "",
            "![Status: Live]"
            + "(https://img.shields.io/badge/status-live-brightgreen)",
            "![LastUpdated](https://img.shields.io/badge"
            + f"/last_updated-{time_updated_for_badge}-green)",
            "",
        ]

    def get_lines_introduction(self) -> list[str]:
        return [
            "Realtime Data about *River Water Levels*"
            + " in Sri Lanka,"
            + f" from the [Irrigation Deptartment]({self.URL_IRRIGATION})'s"
            + f" [Hydrology and Disaster Management]({self.URL_HYDROLOGY})"
            + " Division.",
            "",
            f"- [Complete Dataset]({self.URL_DATA})"
            + f" with **{len(self.rwld_list):,} measurements**"
            + f" from **{len(self.station_to_rwld_list):,}** stations.",
            f"- [Scrape and load logic]({self.URL_LOADER})",
            f"- [Original Data source]({self.URL_ARCGIS_DASHBOARD})",
            "",
        ]

    def get_lines_latest(self) -> list[str]:
        T_RECENT_HOURS = 1
        recent_time_ut = Time.now().ut - T_RECENT_HOURS * 3600
        latest = [
            rwld for rwld in self.rwld_list if rwld.time_ut > recent_time_ut
        ]
        n_latest = len(latest)
        lines = [
            "## Latest measurements",
            "",
            f"*There were **{n_latest:,}** measurements"
            + f" in the last **{T_RECENT_HOURS} hour**.*",
            "",
        ]
        lines.extend(
            Markdown.table(
                [
                    {
                        "Measured At": TimeFormat.TIME.format(
                            Time(
                                rwld.time_ut,
                            )
                        ),
                        "Station (River Basin)": f"{rwld.station_name}"
                        + f" ({rwld.station.river.basin.name})",
                        "Level (m)": f"{rwld.water_level_m:.2f}",
                        "Alert Level": f"{rwld.alert.emoji} {rwld.alert.name}",
                    }
                    for rwld in latest
                ]
            )
        )
        return lines

    def get_lines_latest_by_station(self) -> list[str]:
        d_list = []
        for rwld_list in self.station_to_rwld_list.values():
            latest = rwld_list[0]
            d_list.append(latest)

        lines = ["## Latest by Station", ""]
        lines.extend(
            Markdown.table(
                [
                    {
                        "Measured At": TimeFormat.TIME.format(
                            Time(
                                rwld.time_ut,
                            )
                        ),
                        "Station (River)": f"{rwld.station_name}"
                        + f" ({rwld.station.river.name})",
                        "Level (m)": f"{rwld.water_level_m:.2f}",
                        "Alert Level": f"{rwld.alert.emoji} {rwld.alert.name}",
                    }
                    for rwld in d_list
                ]
            )
        )
        return lines

    def get_lines_footer(self) -> list[str]:
        return [
            "![Maintainer]"
            + "(https://img.shields.io/badge/maintainer-nuuuwan-red)",
            "![MadeWith]"
            + "(https://img.shields.io/badge/made_with-python-blue)",
            "[![License: MIT]"
            + "(https://img.shields.io/badge/License-MIT-yellow.svg)]"
            + "(https://opensource.org/licenses/MIT)",
        ]

    def get_lines_chart_map(self) -> list[str]:
        chart_map_path = ChartMap().draw_map()
        return [
            "## River Water Level Map",
            "",
            f"![River Water Level Map]({chart_map_path})",
            "",
        ]

    def get_lines(self) -> list[str]:
        return (
            self.get_lines_header()
            + self.get_lines_introduction()
            + self.get_lines_latest()
            + self.get_lines_latest_by_station()
            + self.get_lines_chart_map()
            + self.get_lines_footer()
        )

    def build(self):
        lines = self.get_lines()
        readme_file = File(self.PATH)
        readme_file.write_lines(lines)
        log.info(f"Wrote {readme_file}")
