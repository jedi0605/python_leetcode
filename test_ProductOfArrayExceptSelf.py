import unittest
from ProductOfArrayExceptSelf import Solution


class Test_ProductOfArrayExceptSelf(unittest.TestCase):
    def test_case1(self):
        nums = [1, 2, 3, 4]
        solution = Solution()
        res = solution.productExceptSelf2(nums)
        ans = [24, 12, 8, 6]
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
