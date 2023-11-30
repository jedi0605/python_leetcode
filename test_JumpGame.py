import unittest
from JumpGame import Solution


class test_JumpGame(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [2, 3, 1, 1, 4]
        res = solution.canJump(nums)
        self.assertEqual(res, True)

    def test_case2(self):
        solution = Solution()
        nums = [3, 2, 1, 0, 4]
        res = solution.canJump(nums)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()
