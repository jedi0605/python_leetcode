import unittest
from Combinations import Solution


class Combinations_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        res = sol.combine(4, 2)


if __name__ == "__main__":
    unittest.main()
