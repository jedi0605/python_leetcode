import unittest
from ThreeSum import Solution


class test_TwoSumII(unittest.TestCase):
    def test_case1(self):
        numbers = [-1, 0, 1, 2, -1, -4]

        solution = Solution()
        res = solution.threeSum(numbers)
        ans = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(res), sorted(ans))


if __name__ == "__main__":
    unittest.main()
