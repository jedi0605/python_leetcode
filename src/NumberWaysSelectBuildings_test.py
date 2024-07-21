import unittest
from NumberWaysSelectBuildings import Solution


class NumberWaysSelectBuildings_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        s = "001101"
        assert sol.numberOfWays(s) == 6


if __name__ == "__main__":
    unittest.main()
