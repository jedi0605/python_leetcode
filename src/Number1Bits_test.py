import unittest
from Number1Bits import Solution


class Number1Bits_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        assert sol.hammingWeight(11) == 3


if __name__ == "__main__":
    unittest.main()
