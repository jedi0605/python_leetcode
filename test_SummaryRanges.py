from typing import List
import unittest
from SummaryRanges import Solution


class test_SummaryRanges(unittest.TestCase):
    def testcase1(self):
        solution = Solution()
        nums = [0, 1, 2, 4, 5, 7]
        res = solution.summaryRanges(nums)
        ans = ["0->2", "4->5", "7"]
        for i in range(len(ans)):
            assert res[i] == ans[i]


def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
