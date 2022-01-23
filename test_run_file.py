import unittest
from functions import convert_temperatures
from functions import convert_time_local


class TestRunFile(unittest.TestCase):

    def test_temperature_convert(self):
        check_result = convert_temperatures("33 C")
        check_result2 = convert_temperatures("33c")
        check_result3 = convert_temperatures("33 c")
        check_result4 = convert_temperatures("91 F")
        self.assertEqual(check_result, "91F")
        self.assertEqual(check_result2, "91F")
        self.assertEqual(check_result3, "91F")
        self.assertEqual(check_result4, "33C")

    def test_covert_time_local(self):
        check_result_time = convert_time_local("Sofia,  2021-08-01T13:00:00+02:00, 33c")
        result_time = convert_time_local("Sofia, 2021-08-01T13:00:00+02:00, 33 C")
        check_result_time1 = convert_time_local("Varna, 2021-08-01T11:45:00Z,25 C")
        result_time1 = convert_time_local("Varna, 2021-08-01T11:45:00Z,25 C")
        self.assertEqual(check_result_time, result_time)
        self.assertEqual(check_result_time1, result_time1)



if __name__ == '__main__':
    unittest.main()
