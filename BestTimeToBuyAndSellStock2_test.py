import unittest
from BestTimeToBuyAndSellStockII import Solution


class Test_BestTimeToBuyAndSellStockII(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [7, 1, 5, 3, 6, 4]
        ans = 7
        res = solution.maxProfit(nums)
        assert res == ans

    def test_case2(self):
        solution = Solution()
        nums = [7, 6, 5, 4, 3]
        ans = 0
        res = solution.maxProfit(nums)
        assert res == ans


if __name__ == "__main__":
    unittest.main()
