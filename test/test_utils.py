import unittest
from utils.file_parser import *
from utils.time_parser import *


class TestUtils(unittest.TestCase):
    # File parser
    def test_read_parse_file(self):
        result = ["RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
                  "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
                  "LUIS=MO10:00-20:00,TH12:00-14:00,SU20:00-21:00",
                  "JUAN=MO08:00-19:00,TH12:00-14:00,SU20:00-21:00",
                  "MARI=MO22:00-01:00,TH12:00-14:00,SU20:00-21:00"]
        self.assertEqual(read_parse_file("../work_info.txt"), result)

    def test_validate_info(self):
        line1 = "MARI=MO22:00-01:00,TH12:00-14:00,SU20:00-21:00"
        self.assertEqual(validate_info(line1).string, line1)
        line2 = "MARI=tO22:00-01:00,TH12:00-14:00,SU20:00-21:00"
        self.assertEqual(validate_info(line2), None)

    # Time parser
    def test_to_24_hours(self):
        hour1 = timedelta(hours=0)
        result1 = timedelta(hours=24)
        self.assertEqual(to_24_hours(hour1), result1)
        hour2 = timedelta(hours=24)
        self.assertEqual(to_24_hours(hour2), hour2)

    def test_hour_to_number(self):
        hour = timedelta(hours=14, minutes=12, seconds=33, microseconds=99)
        self.assertEqual(hour_to_number(hour), 14)


if __name__ == '__main__':
    unittest.main()
