import unittest
from RestoreIPAddresses import Solution
from ListNode import ListNode


class RestoreIPAddresses_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s ="25525511135"
        solution.restoreIpAddresses(s)


if __name__ == "__main__":
    unittest.main()
