import unittest
from MinimumAdjacentSwapsMakeValidArray import Solution


class MinimumGeneticMutation_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [3, 4, 5, 5, 3, 1]
        assert solution.minimumSwaps(nums) == 6


if __name__ == "__main__":
    unittest.main()
