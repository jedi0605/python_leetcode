import unittest
from typing import List
from InsertInterval import Solution

class test_InsertInterval(unittest.TestCase):
    def test1(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        s = Solution()
        res = s.insert(intervals,newInterval)
        ans = [[1,5],[6,9]]
        assert compare_lists_of_lists(res,ans) == True
        
def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == '__main__':
    unittest.main()
