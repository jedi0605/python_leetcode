from typing import List
import unittest
from ContainsDuplicateII import Solution


class test_containsDuplicate(unittest.TestCase):
    def testcase1(self):
        solution = Solution()
        nums = [1, 2, 3, 1]
        k = 3
        assert solution.containsNearbyDuplicate(nums, k) == True

    def testcase2(self):
        solution = Solution()
        nums = [1, 0, 1, 1]
        k = 1
        assert solution.containsNearbyDuplicate(nums, k) == True

    def testcase3(self):
        solution = Solution()
        nums = [1, 2, 3, 1, 2, 3]
        k = 2
        assert solution.containsNearbyDuplicate(nums, k) == False


def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
