import unittest
from TheNumberBeautifulSubsets import Solution


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):

        sol = Solution()
        nums =[2,2]
        k = 2
        res = sol.beautifulSubsets(nums,k)
        assert res == 3


if __name__ == "__main__":
    unittest.main()
