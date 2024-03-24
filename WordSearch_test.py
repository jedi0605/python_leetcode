import unittest
from WordSearch import Solution


class test_ZigzagConversion(unittest.TestCase):
    def test_case1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        sol = Solution()
        assert sol.exist(board,word) 


if __name__ == "__main__":
    unittest.main()
