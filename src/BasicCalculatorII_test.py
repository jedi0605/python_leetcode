import unittest
from BasicCalculatorII import Solution


class BasicCalculatorII_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = " 3+5/2"
        assert solution.calculate(s) == 5
        
if __name__ == "__main__":
    unittest.main()
