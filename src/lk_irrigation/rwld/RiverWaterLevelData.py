from dataclasses import dataclass
from functools import cached_property

from utils import Log

from lk_irrigation.base.HasTimeMixin import HasTimeMixin
from lk_irrigation.core.Station import Station
from lk_irrigation.rwld.RiverWaterLevelDataFileMixin import \
    RiverWaterLevelDataFileMixin
from lk_irrigation.rwld.RiverWaterLevelDataLoadMixin import \
    RiverWaterLevelDataLoadMixin

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
