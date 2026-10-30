# D. Create a unit test file named test.py that executes three tests run against your code.
import unittest
from weather import Weather, Weather_DB


class FakeWeather:
    def __init__(self):
        self.lat = 43.55
        self.lon = -96.73
        self.month = 7
        self.day = 4
        self.year = 2026
        self.five_year_mean_temp = 70.0
        self.five_year_min_temp = 60.0
        self.five_year_max_temp = 80.0
        self.five_year_mean_wind = 10.0
        self.five_year_min_wind = 4.0
        self.five_year_max_wind = 16.0
        self.five_year_sum_precip = 1.0
        self.five_year_min_precip = 0.2
        self.five_year_max_precip = 0.2


class TestWeather(unittest.TestCase):
    def test_get_mean_temp(self):
        weather = Weather.__new__(Weather)
        weather.five_year_mean_temp = 70.0
        self.assertEqual(weather.get_mean_temp(), 70.0)

    def test_get_max_wind(self):
        weather = Weather.__new__(Weather)
        weather.five_year_max_wind = 16
        self.assertEqual(weather.get_max_wind(), 16)

    def test_get_precip_sum(self):
        weather = Weather.__new__(Weather)
        weather.five_year_sum_precip = 1.0
        self.assertEqual(weather.get_precip_sum(), 1.0)

if __name__ == "__main__":
    unittest.main()
