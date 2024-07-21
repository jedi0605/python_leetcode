import unittest
from RomanToInteger import Solution


class test_romanToInteger(unittest.TestCase):
    def test_case1(self):
        s ="III"
        solution = Solution()        
        assert solution.romanToInt(s) == 3

    def test_case2(self):
        s ="LVIII"
        solution = Solution()        
        assert solution.romanToInt(s) == 58
    def test_case2(self):
        s ="MCMXCIV"
        solution = Solution()        
        assert solution.romanToInt(s) == 1994


if __name__ == "__main__":
    unittest.main()
