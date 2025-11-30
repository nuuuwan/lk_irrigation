from utils import Log

from lk_irrigation.rwld.RiverWaterLevelDataFileReadOnlyMixin import (
    RiverWaterLevelDataFileReadOnlyMixin,
)
from lk_irrigation.rwld.RiverWaterLevelDataFileWriteMixin import (
    RiverWaterLevelDataFileWriteMixin,
)

log = Log("RiverWaterLevelDataFileMixin")


class RiverWaterLevelDataFileMixin(
    RiverWaterLevelDataFileWriteMixin, RiverWaterLevelDataFileReadOnlyMixin
):
    pass
