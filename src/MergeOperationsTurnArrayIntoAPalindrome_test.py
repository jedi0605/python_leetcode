import unittest
from MergeOperationsTurnArrayIntoAPalindrome import Solution


class MergeOperationsTurnArrayIntoAPalindrome_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [4, 3, 2, 1, 2, 3, 1]
        assert solution.minimumOperations(nums) == 2


if __name__ == "__main__":
    unittest.main()
