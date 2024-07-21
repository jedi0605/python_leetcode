import unittest
from KidsWithGreatestNumberCandies import Solution


class KidsWithGreatestNumberCandies_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        assert solution.kidsWithCandies(candies, extraCandies) == [
            True,
            True,
            True,
            False,
            True,
        ]


if __name__ == "__main__":
    unittest.main()
