import unittest
from RemoveDuplicatesfromSortedListII import Solution
from ListNode import ListNode


class test_ReverseLinkedListII(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        # Example usage:
        head = [1, 2, 3, 3, 4, 4, 5]
        list1 = ListNode.array_to_linked_list(head)
        res = solution.deleteDuplicates(list1)
        a = [1, 2, 5]
        ans = ListNode.array_to_linked_list(a)
        assert ListNode.are_linked_lists_equal(res, ans)


if __name__ == "__main__":
    unittest.main()
