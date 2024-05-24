import unittest
from SearchRotatedSortedArray import Solution


class SearchRotatedSortedArray_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 0
        assert sol.search(nums,target) == 4


if __name__ == "__main__":
    unittest.main()
