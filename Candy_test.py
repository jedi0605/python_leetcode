import unittest
from Candy import Solution


class test_Candy(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        rating = [1, 0, 2]
        res = solution.candy(rating)
        assert res == 5

    def test_case2(self):
        solution = Solution()
        rating = [5, 4, 3, 5, 6, 2]
        res = solution.candy(rating)
        assert res == 12


if __name__ == "__main__":
    unittest.main()
