import unittest
from ReverseLinkedListII import Solution
from ListNode import ListNode


class test_ReverseLinkedListII(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        # Example usage:
        l1 = [1, 2, 3, 4, 5]
        left, right = 2, 4
        list1 = ListNode.array_to_linked_list(l1)
        res = solution.reverseBetween(list1, left, right)
        a = [1, 4, 3, 2, 5]
        ans = ListNode.array_to_linked_list(a)
        assert ListNode.are_linked_lists_equal(res, ans)


if __name__ == "__main__":
    unittest.main()
