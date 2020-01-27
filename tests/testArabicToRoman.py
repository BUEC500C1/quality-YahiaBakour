import sys, os
import unittest
sys.path.insert(0,os.path.dirname(os.path.dirname(__file__)))
from arabicToRoman import arabicToRoman

class BasicTests(unittest.TestCase):
    def test_arabic_to_roman(self):           
        assert (arabicToRoman("1") == "I")
        assert (arabicToRoman("230") == "CCXXX")
        assert (arabicToRoman("432") == "CDXXXII")

if __name__ == '__main__':
    unittest.main()