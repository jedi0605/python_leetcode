import unittest
from PowXN import Solution


class PowXN_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        assert sol.myPow(2,10) == 1024


if __name__ == "__main__":
    unittest.main()
