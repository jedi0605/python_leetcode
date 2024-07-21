import unittest
from RemoveDuplicatesSortedArrayII import Solution


class RemoveDuplicatesSortedArrayII_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        # Example usage:
        nums = [1,1,1,2,2,3]
        assert solution.removeDuplicates(nums) == 5


if __name__ == "__main__":
    unittest.main()
