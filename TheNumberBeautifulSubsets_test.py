import unittest
from TheNumberBeautifulSubsets import Solution


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):

        sol = Solution()
        nums = [2,4,6]
        k = 2
        assert sol.beautifulSubsets(nums,k) == 4


if __name__ == "__main__":
    unittest.main()
