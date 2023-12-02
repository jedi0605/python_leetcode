import unittest
from Hindex import Solution


class Test_Hindex(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [3, 0, 6, 1, 5]
        res = solution.hIndex2(nums)
        assert res == 3


if __name__ == "__main__":
    unittest.main()
