import unittest
from FindMinimumTimeFinishAllJobsII import Solution


class test_FlattenBinaryTreetoLinkedList(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        jobs = [5, 2, 4]
        workers = [1, 7, 5]
        assert solution.minimumTime(jobs, workers) == 2


if __name__ == "__main__":
    unittest.main()
