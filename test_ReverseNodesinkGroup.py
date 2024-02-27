import unittest
from ReverseNodesinkGroup import Solution
from ListNode import ListNode


class test_ReverseNodesinkGroup(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        # Example usage:
        l1 = [1, 2, 3, 4, 5]
        k = 2
        list1 = ListNode.array_to_linked_list(l1)
        res = solution.reverseKGroup(list1, k)
        ans = ListNode.array_to_linked_list([2, 1, 4, 3, 5])
        assert ListNode.are_linked_lists_equal(res, ans)


if __name__ == "__main__":
    unittest.main()
