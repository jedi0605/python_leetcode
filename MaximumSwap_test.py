import unittest
from MaximumSwap import Solution
from ListNode import ListNode


class MaximumSwap_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        assert solution.maximumSwap(867736) == 877636


if __name__ == "__main__":
    unittest.main()
