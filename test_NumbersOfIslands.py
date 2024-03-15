import unittest
from NumberofIslands import Solution


class test_NumbersOfIslands(unittest.TestCase):
    def test_case1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        sol = Solution()
        assert sol.numIslands(grid) == 1

    def test_case2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        sol = Solution()
        assert sol.numIslands(grid) == 3


if __name__ == "__main__":
    unittest.main()
