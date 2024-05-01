import unittest
from ThekthFactorOfN import Solution


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):
        
        sol = Solution()
        n=12
        k=3
        assert sol.kthFactor(n,k) == 3


if __name__ == "__main__":
    unittest.main()
