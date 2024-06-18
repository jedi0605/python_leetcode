import unittest
from RemoveElement import Solution
from ListNode import ListNode


class RemoveElement_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        # Example usage:
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        solution.removeElement(nums, val)


if __name__ == "__main__":
    unittest.main()
