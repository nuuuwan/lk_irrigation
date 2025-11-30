from dataclasses import dataclass
from functools import cached_property

from utils import Log

from lk_irrigation.base.HasTimeMixin import HasTimeMixin
from lk_irrigation.core import Alert
from lk_irrigation.core.Station import Station
from lk_irrigation.rwld.RiverWaterLevelDataFileMixin import (
    RiverWaterLevelDataFileMixin,
)
from lk_irrigation.rwld.RiverWaterLevelDataLoadMixin import (
    RiverWaterLevelDataLoadMixin,
)

log = Log("RiverWaterLevelData")


@dataclass
class RiverWaterLevelData(
    HasTimeMixin, RiverWaterLevelDataLoadMixin, RiverWaterLevelDataFileMixin
):
    station_name: str
    time_ut: int
    water_level_m: float

    @cached_property
    def station(self):
        return Station.from_name(self.station_name)

    @cached_property
    def alert(self):  # noqa: CFQ004
        if self.water_level_m >= self.station.major_flood_level_m:
            return Alert.MAJOR
        if self.water_level_m >= self.station.minor_flood_level_m:
            return Alert.MINOR
        if self.water_level_m >= self.station.alert_level_m:
            return Alert.ALERT
        return Alert.NORMAL
