import unittest
from JumpGameII import Solution


class test_JumpGameII(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        nums = [2, 3, 1, 1, 4]
        res = solution.jump(nums)
        self.assertEqual(res, 2)


if __name__ == "__main__":
    unittest.main()
