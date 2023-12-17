import unittest
from TwoSumII import Solution


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        solution = Solution()
        assert solution.twoSum(numbers, target) == [1, 2]
        


if __name__ == "__main__":
    unittest.main()
