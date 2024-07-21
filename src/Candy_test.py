import unittest
from Candy import Solution


class test_Candy(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        rating = [1, 2, 2]
        res = solution.candy(rating)
        assert res == 4

    def test_case2(self):
        solution = Solution()
        rating = [1,2,87,87,87,2,1]
        res = solution.candy(rating)
        assert res == 13


if __name__ == "__main__":
    unittest.main()
