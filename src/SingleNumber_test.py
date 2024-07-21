import unittest
from SingleNumber import Solution


class SingleNumber_test(unittest.TestCase):
    def test_case1(self):

        sol = Solution()
        nums = [4, 1, 2, 1, 2]
        assert sol.singleNumber(nums) == 4


if __name__ == "__main__":
    unittest.main()
