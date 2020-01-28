import sys, os
import unittest
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
from arabicToRoman import arabicToRoman

class BasicTests(unittest.TestCase):
    def test_arabic_to_roman(self):           
        assert (arabicToRoman("1") == "I")
        assert (arabicToRoman("230") == "CCXXX")
        assert (arabicToRoman("432") == "CDXXXII")
    def test_invalid_input(self):
        try:
            arabicToRoman("!!!")
            self.fail("Exception wasn't raised")
        except ValueError as e:
            pass
        try:
            arabicToRoman("ABC")
            self.fail("Exception wasn't raised")
        except ValueError as e:
            pass
        try:
            arabicToRoman("4000")
            self.fail("Exception wasn't raised")
        except Exception as e:
            pass
        try:
            arabicToRoman("-3")
            self.fail("Exception wasn't raised")
        except Exception as e:
            pass
if __name__ == '__main__':
    unittest.main()