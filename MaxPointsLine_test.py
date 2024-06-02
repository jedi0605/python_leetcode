import unittest
from MaxPointsLine import Solution
from ListNode import ListNode


class MaximumSwap_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()       
        points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        assert solution.maxPoints(points) == 4


if __name__ == "__main__":
    unittest.main()
