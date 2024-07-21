import unittest
from MaximumProfitJobScheduling import Solution


class MaximumProfitJobScheduling_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        startTime = [1, 2, 3, 4, 6]

        endTime = [3, 5, 10, 6, 9]
        profit = [20, 20, 100, 70, 60]
        assert solution.jobScheduling(startTime, endTime, profit) == 150

    def test_case2(self):
        solution = Solution()
        startTime = [1, 2, 3, 3]
        endTime = [3, 4, 5, 6]
        profit = [50, 10, 40, 70]
        assert solution.jobScheduling(startTime, endTime, profit) == 150


if __name__ == "__main__":
    unittest.main()
