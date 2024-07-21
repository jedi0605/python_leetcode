import unittest
from ListNode import ListNode
from MergeKSortedLists import Solution


class MergeKSortedLists_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        lists = [
            ListNode.array_to_linked_list([1, 4, 5]),
            ListNode.array_to_linked_list([1, 3, 4]),
            ListNode.array_to_linked_list([2, 6]),
        ]
        ans = ListNode.array_to_linked_list([1, 1, 2, 3, 4, 4, 5, 6])
        assert ListNode.are_linked_lists_equal(solution.mergeKLists(lists), ans)


if __name__ == "__main__":
    unittest.main()
