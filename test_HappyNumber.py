from typing import List
import unittest
from HappyNumber import Solution


class test_HappyNumber(unittest.TestCase):
    def testcase1(self):
        solution = Solution()
        assert solution.isHappy(19) == True
    
    def testcase2(self):
        solution = Solution()
        assert solution.isHappy(2) == False

def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
