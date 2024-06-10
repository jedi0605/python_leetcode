import unittest
from BestTimeBuySellStockIII import Solution


class BestTimeBuySellStockIII_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        prices = [3,3,5,0,0,3,1,4]
        
        assert solution.maxProfit(prices) == 6

    def test_case2(self):
        solution = Solution()
        nums = [7, 6, 5, 4, 3]
        ans = 0
        res = solution.maxProfit(nums)
        assert res == ans


if __name__ == "__main__":
    unittest.main()
