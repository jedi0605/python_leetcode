import unittest
from ReverseBits import Solution


class ReverseBits_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = 43261596 # 00000010100101000001111010011100
        assert solution.reverseBits(s) == 964176192


if __name__ == "__main__":
    unittest.main()
