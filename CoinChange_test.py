import unittest
from CoinChange import Solution


class CoinChange_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        coins = [1,2,5]
        amount = 11
        assert sol.coinChange(coins,amount) == 3


if __name__ == "__main__":
    unittest.main()
