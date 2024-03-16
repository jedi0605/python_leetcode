import unittest
from IntegerToRoman import Solution


class test_IntegerToRoman(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        assert solution.intToRoman(1994) == "MCMXCIV"
        assert solution.intToRoman(58) == "LVIII"
        assert solution.intToRoman(3) == "III"


if __name__ == "__main__":
    unittest.main()
