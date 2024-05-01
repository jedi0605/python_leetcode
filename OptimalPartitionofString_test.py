import unittest
from OptimalPartitionofString import Solution


class OptimalPartitionofString_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        s = "abacaba"
        assert sol.partitionString(s) == 4


if __name__ == "__main__":
    unittest.main()
