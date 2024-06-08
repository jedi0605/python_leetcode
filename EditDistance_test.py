import unittest
from EditDistance import Solution


class EditDistance_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        word1 = "horse"
        word2 = "ros"
        assert sol.minDistance(word1, word2) == 3


if __name__ == "__main__":
    unittest.main()
