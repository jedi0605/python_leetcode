import unittest
from AddStrings import Solution
from ListNode import ListNode


class AddStrings_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        assert solution.addStrings("1","9") == "10"


if __name__ == "__main__":
    unittest.main()
