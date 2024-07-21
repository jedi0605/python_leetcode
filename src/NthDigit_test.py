import unittest
from NthDigit import Solution


class test_NumbersOfIslands(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        assert sol.findNthDigit(99) == 4


if __name__ == "__main__":
    unittest.main()
