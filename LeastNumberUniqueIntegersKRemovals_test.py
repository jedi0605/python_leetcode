import unittest
from LeastNumberUniqueIntegersKRemovals import Solution


class LeastNumberUniqueIntegersKRemovals_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        arr = [5, 5, 4]
        k = 1
        assert solution.findLeastNumOfUniqueInts(arr,k) == 1


if __name__ == "__main__":
    unittest.main()
