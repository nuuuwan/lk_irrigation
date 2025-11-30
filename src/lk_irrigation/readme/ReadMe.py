from utils import File, Format, Log, Time, TimeFormat

from lk_irrigation.base import Markdown
from lk_irrigation.charts.ChartMap import ChartMap
from lk_irrigation.charts.ChartStation import ChartStation
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
    T_LATE_HOURS = 24

    def __init__(self):
        self.rwld_list = RiverWaterLevelData.list_all()
        self.station_to_rwld_list = RiverWaterLevelData.station_to_list()
        self.station_to_latest = RiverWaterLevelData.station_to_latest()
        self.station_to_ror = RiverWaterLevelData.station_to_ror()
        self.latest_sorted = sorted(
            self.station_to_latest.values(),
            key=lambda d: (
                d.alert.level,
                self.station_to_ror[d.station_name],
            ),
            reverse=True,
        )

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

    def get_markdown_for_rwld(self, rwld) -> dict:
        ror = self.station_to_ror[rwld.station_name]
        rising_alert = "🔺 Rising" if ror > 0.005 else ""
        min_time_recent = Time.now().ut - self.T_LATE_HOURS * 3600
        time_emoji = "⌛" if rwld.time_ut < min_time_recent else ""
        return {
            "Measured At": TimeFormat.TIME.format(
                Time(
                    rwld.time_ut,
                )
            )
            + time_emoji,
            "Station (River Basin)": f"{rwld.station_name}"
            + f" ({rwld.station.river.basin.name})",
            "Level (m)": f"{rwld.water_level_m:.2f}",
            "Alert Level": f"{rwld.alert.emoji} {rwld.alert.name}",
            "Rate-of-Rise (m/hr)": f"{ror:.3f}",
            "Rising Alert": rising_alert,
        }

    def get_lines_latest(self) -> list[str]:
        T_RECENT_HOURS = 1
        recent_time_ut = Time.now().ut - T_RECENT_HOURS * 3600

        latest = [
            rwld for rwld in self.rwld_list if (rwld.time_ut > recent_time_ut)
        ]
        latest.reverse()
        n_latest = len(latest)

        lines = [
            "## Latest measurements",
            "",
            f"*There were **{n_latest:,}** measurements"
            + f" in the last **{T_RECENT_HOURS} hour**.*",
            "",
        ]
        if n_latest > 0:
            lines.extend(
                Markdown.table(
                    [self.get_markdown_for_rwld(rwld) for rwld in latest]
                )
            )
        return lines

    def get_lines_latest_by_station(self) -> list[str]:
        lines = [
            "## Latest by Station",
            "",
            "*⌛ = Latest measurement"
            + f" is older than **{self.T_LATE_HOURS} hours**.*",
            "",
        ]
        lines.extend(
            Markdown.table(
                [
                    self.get_markdown_for_rwld(rwld)
                    for rwld in self.latest_sorted
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

    def get_lines_map(self) -> list[str]:
        chart_map_path = ChartMap().draw_map()
        return [
            "## River Water Level Map",
            "",
            f"![River Water Level Map]({chart_map_path})",
            "",
        ]

    def get_lines_charts_for_stations(self) -> list[str]:
        station_to_image = ChartStation.draw_all_stations()
        lines = ["## River Water Level Charts by Station", ""]
        for rwld in self.latest_sorted:
            station_name = rwld.station_name
            image_path = station_to_image[station_name]
            lines.extend(
                [
                    f"### {station_name} ({rwld.station.river.basin.name})",
                    "",
                    f"![{station_name}]({image_path})",
                    "",
                ]
            )
        return lines

    def get_lines(self) -> list[str]:
        return (
            self.get_lines_header()
            + self.get_lines_introduction()
            + self.get_lines_map()
            + self.get_lines_latest()
            + self.get_lines_latest_by_station()
            + self.get_lines_charts_for_stations()
            + self.get_lines_footer()
        )

    def build(self):
        lines = self.get_lines()
        readme_file = File(self.PATH)
        readme_file.write_lines(lines)
        log.info(f"Wrote {readme_file}")
