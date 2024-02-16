from typing import List
import unittest
from LongestConsecutiveSequence import Solution


class test_containsDuplicate(unittest.TestCase):
    def testcase1(self):
        solution = Solution()
        nums = [100,4,200,1,3,2]
        assert solution.longestConsecutive(nums) == 4

def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
