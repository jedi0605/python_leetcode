import unittest
from BestTimeBuySellStockIV import Solution


class BestTimeBuySellStockIV_Test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        k = 2
        prices = [3,2,6,5,0,3]

        assert solution.maxProfit(k, prices) == 7



if __name__ == "__main__":
    unittest.main()
