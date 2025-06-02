import unittest

def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            return True
    return False

class TestIsLeapYear(unittest.TestCase):

    def test_leap_years(self):
        self.assertTrue(is_leap_year(2000)) 
        self.assertTrue(is_leap_year(2016))
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(2400))

    def test_non_leap_years(self):
        self.assertFalse(is_leap_year(1900)) 
        self.assertFalse(is_leap_year(2019))
        self.assertFalse(is_leap_year(2021))
        self.assertFalse(is_leap_year(1800))

if __name__ == '__main__':
    unittest.main()
