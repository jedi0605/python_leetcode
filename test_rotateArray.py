import unittest
from RotateArray import Solution


class Test_RotateArray(unittest.TestCase):
    def test_rotate(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        solution.rotate(nums, k)
        ans = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(nums, ans)

    def test_rotate2(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        solution.rotate2(nums, k)
        ans = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(nums, ans)


if __name__ == "__main__":
    unittest.main()
