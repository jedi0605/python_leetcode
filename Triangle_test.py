from typing import List
import unittest
from Triangle import Solution


class Triangle_test(unittest.TestCase):
    def testcase1(self):
        solution = Solution()
        triangle = [[-1], [3, 2], [-3, 1, -1]]
        assert solution.minimumTotal(triangle) == -1


def compare_lists_of_lists(list1: List[List[str]], list2: List[List[str]]) -> bool:
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
