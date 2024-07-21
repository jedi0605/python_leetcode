from typing import List
import unittest
from LongestIncreasingSubsequence import Solution


class test_containsDuplicate(unittest.TestCase):
    def testcase1(self):
        arr = [10, 9, 2, 5, 3, 7, 101, 18]
        solution = Solution()
        assert solution.lengthOfLIS(arr) == 4


def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
