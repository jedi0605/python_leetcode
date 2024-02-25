import unittest
from MergeTwoSortedLists import Solution
from ListNode import ListNode


class test_MergeTwoSortedLists(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        ListNode
        # Example usage:
        l1 = [1, 2, 4]
        l2 = [1, 3, 4]
        list1 = ListNode.array_to_linked_list(l1)
        list2 = ListNode.array_to_linked_list(l2)
        res = solution.mergeTwoLists(list1, list2)
        a = [1, 1, 2, 3, 4, 4]
        ans = ListNode.array_to_linked_list(a)
        assert ListNode.are_linked_lists_equal(res, ans)


if __name__ == "__main__":
    unittest.main()
