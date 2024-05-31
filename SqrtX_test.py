import unittest
from SqrtX import Solution


class SubarraySumEqualsK_test(unittest.TestCase):
    def test_case1(self):
       
        solution = Solution()
        assert solution.mySqrt(10) == 3


if __name__ == "__main__":
    unittest.main()
