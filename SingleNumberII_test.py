import unittest
from SingleNumberII import Solution


class SingleNumber_test(unittest.TestCase):
    def test_case1(self):

        sol = Solution()
        nums = [1, 1,  1, 2]
        assert sol.singleNumber(nums) == 2


if __name__ == "__main__":
    unittest.main()
