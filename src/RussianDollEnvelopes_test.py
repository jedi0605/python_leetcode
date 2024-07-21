from typing import List
import unittest
from RussianDollEnvelopes import Solution


class RussianDollEnvelopes_test(unittest.TestCase):
    def testcase1(self):
        envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        solution = Solution()
        assert solution.maxEnvelopes(envelopes) == 3

    def testcase2(self):
        result = [1, 3, 5, 7, 9]
        e = 6
        
        l, r = 0, len(result) - 1
        while l <= r:
            mid = (l + r) >> 1
            if result[mid] >= e:
                r = mid - 1

            else:
                l = mid + 1
        assert l == 3

def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
