import unittest
from BasicCalculator import Solution


class test_BasicCalculator(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "1 + 1"
        assert solution.calculate(s) == 2
        s = "(1+(4+5+2)-3)+(6+8)"
        assert solution.calculate(s) == 23

if __name__ == "__main__":
    unittest.main()
