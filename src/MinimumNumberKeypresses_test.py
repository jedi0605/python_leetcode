import unittest
from MinimumNumberKeypresses import Solution


class MinimumNumberKeypresses_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "abcdefghijkl"
        assert solution.minimumKeypresses(s) == 15

if __name__ == "__main__":
    unittest.main()
