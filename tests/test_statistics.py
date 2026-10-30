
import unittest

from netwatch.statistics import calculate_statistics


class TestCalculateStatistics(unittest.TestCase):

    def test_all_measurements_succeed(self):
        results = [
            {"success": True, "latency": 100, "error": None},
            {"success": True, "latency": 200, "error": None},
        ]

        stats = calculate_statistics(results)

        self.assertEqual(stats["successful_count"], 2)
        self.assertEqual(stats["failed_count"], 0)
        self.assertEqual(stats["average"], 150)
        self.assertEqual(stats["minimum"], 100)
        self.assertEqual(stats["maximum"], 200)


    def test_mixed_success_and_failure(self):
        results = [
            {"success": True, "latency": 100, "error": None},
            {"success": False, "latency": None, "error": "Connection timed out"},
            {"success": True, "latency": 200, "error": None},
        ]

        stats = calculate_statistics(results)

        self.assertEqual(stats["successful_count"], 2)
        self.assertEqual(stats["failed_count"], 1)
        self.assertEqual(stats["average"], 150)
        self.assertEqual(stats["minimum"], 100)
        self.assertEqual(stats["maximum"], 200)

    def test_all_measurements_fail(self):
        results = [
            {"success": False, "latency": None, "error": "Timeout"},
            {"success": False, "latency": None, "error": "Connection refused"},
        ]

        stats = calculate_statistics(results)

        self.assertEqual(stats["successful_count"], 0)
        self.assertEqual(stats["failed_count"], 2)
        self.assertIsNone(stats["average"])
        self.assertIsNone(stats["minimum"])
        self.assertIsNone(stats["maximum"])


if __name__ == "__main__":
    unittest.main()
