import unittest
from AddTwoNumbers import Solution
from ListNode import ListNode


class test_AddTwoNumbers(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        ListNode
        # Example usage:
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        list1 = ListNode.array_to_linked_list(l1)
        list2 = ListNode.array_to_linked_list(l2)
        res = solution.addTwoNumbers(list1, list2)
        a = [7, 0, 8]
        ans = ListNode.array_to_linked_list(a)
        assert ListNode.are_linked_lists_equal(res, ans)


if __name__ == "__main__":
    unittest.main()
