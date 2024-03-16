import unittest
from PartitionList import Solution
from ListNode import ListNode


class test_RotateListList(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        k = 3
        list1 = ListNode.array_to_linked_list([1, 4, 3, 2, 5, 2])
        res = solution.partition(list1, k)
        ans = ListNode.array_to_linked_list([1, 2, 2, 4, 3, 5])
        assert ListNode.are_linked_lists_equal(res, ans)

    def test_case2(self):
        solution = Solution()
        k = 2
        list1 = ListNode.array_to_linked_list([2, 1])
        res = solution.partition(list1, k)
        ans = ListNode.array_to_linked_list([1, 2])
        assert ListNode.are_linked_lists_equal(res, ans)


if __name__ == "__main__":
    unittest.main()
