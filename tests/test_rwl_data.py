import unittest

from lk_irrigation import RiverWaterLevelData


class TestCase(unittest.TestCase):

    @unittest.skip("slow")
    def test_load_station_from_remote(self):
        d_list = RiverWaterLevelData.load_station_from_remote(
            "Nagalagam Street"
        )
        self.assertGreater(len(d_list), 0)

    def test_load_all_from_remote(self):
        d_list = RiverWaterLevelData.load_all_from_remote()
        self.assertGreater(len(d_list), 0)
