import unittest
from AddBinary import Solution
from ListNode import ListNode


class AddStrings_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        assert solution.addBinary("11","1") == "100"


if __name__ == "__main__":
    unittest.main()
