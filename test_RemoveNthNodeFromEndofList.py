import unittest
from RemoveNthNodeFromEndofList import Solution
from ListNode import ListNode


class test_RemoveNthNodeFromEndofList(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        # Example usage:
        k = 2
        list1 = ListNode.array_to_linked_list([1, 2, 3, 4, 5])
        res = solution.removeNthFromEnd(list1, k)
        ans = ListNode.array_to_linked_list([1,2,3,5])
        assert ListNode.are_linked_lists_equal(res, ans)


if __name__ == "__main__":
    unittest.main()
