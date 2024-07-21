from typing import List
import unittest
from TwoSum import Solution


class test_TwoSum(unittest.TestCase):
    def testcase1(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        res = solution.twoSum(nums, target)
        assert res == [0, 1]


def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
