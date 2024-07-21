import unittest
from NumberofProvinces import Solution


class NumberofProvinces_test(unittest.TestCase):
    def test_case1(self):
        isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        sol = Solution()
        assert sol.findCircleNum(isConnected) == 2


if __name__ == "__main__":
    unittest.main()
