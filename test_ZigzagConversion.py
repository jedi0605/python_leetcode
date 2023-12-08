import unittest
from ZigzagConversion import Solution


class test_ZigzagConversion(unittest.TestCase):
    def test_case1(self):
        s = "III"
        solution = Solution()
        assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
        assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


if __name__ == "__main__":
    unittest.main()
