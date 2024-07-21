import unittest
from ListNode import ListNode
from SortList import Solution


class SortList_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        root = ListNode()
        head = [4, 2, 1, 3]
        tmp = root.array_to_linked_list(head)
        sol.sortList(tmp)
        # assert sol.snakesAndLadders(board) == 4


if __name__ == "__main__":
    unittest.main()
