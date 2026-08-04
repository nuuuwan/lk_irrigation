import unittest
from types import SimpleNamespace

from lk_irrigation import Alert, ReadMe


class TestReadMe(unittest.TestCase):
    @staticmethod
    def get_readme(alerts):
        readme = ReadMe.__new__(ReadMe)
        readme.latest_sorted = [
            SimpleNamespace(station_name=station_name, alert=alert)
            for station_name, alert in alerts
        ]
        return readme

    def test_get_lines_summary_lists_important_alerts(self):
        readme = self.get_readme(
            [
                ("Major Station", Alert.MAJOR),
                ("Minor Station", Alert.MINOR),
                ("Normal Station", Alert.NORMAL),
            ]
        )

        summary = "\n".join(readme.get_lines_summary())

        self.assertIn("🔴 Major Station — Major Flood", summary)
        self.assertIn("🟠 Minor Station — Minor Flood", summary)
        self.assertNotIn("Normal Station", summary)
        self.assertIn("Sri Lanka Irrigation Department", summary)
        self.assertIn(ReadMe.URL_REPOSITORY, summary)
        self.assertLess(len(summary), 288)

    def test_get_lines_summary_truncates_alerts_without_truncating_links(self):
        readme = self.get_readme(
            [(f"Very Long Station Name {i}", Alert.ALERT) for i in range(20)]
        )

        summary = "\n".join(readme.get_lines_summary())

        self.assertLess(len(summary), 288)
        self.assertIn("…", summary)
        self.assertIn(ReadMe.URL_IRRIGATION, summary)
        self.assertTrue(summary.endswith(ReadMe.URL_REPOSITORY))

    def test_get_lines_summary_handles_no_active_alerts(self):
        readme = self.get_readme([("Normal Station", Alert.NORMAL)])

        summary = "\n".join(readme.get_lines_summary())

        self.assertIn("No active alerts.", summary)
        self.assertLess(len(summary), 288)
