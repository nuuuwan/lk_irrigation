import unittest

from lk_irrigation import RiverWaterLevelData


class TestCase(unittest.TestCase):

    @unittest.skip("Requires network access")
    def test_load_station_from_remote(self):
        d_list = RiverWaterLevelData.load_station_from_remote(
            "Nagalagam Street", 7, 50, 25
        )
        self.assertGreater(len(d_list), 0)

    @unittest.skip("Requires network access")
    def test_load_all_from_remote(self):
        d_list = RiverWaterLevelData.load_all_from_remote(7, 50, 25)
        self.assertGreater(len(d_list), 0)
