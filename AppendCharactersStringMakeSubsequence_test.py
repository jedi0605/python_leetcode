import unittest
from AppendCharactersStringMakeSubsequence import Solution
from TreeNode import TreeNode


class AppendCharactersStringMakeSubsequence_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "coaching"
        t = "coding"
        assert solution.appendCharacters(s,t) == 4


if __name__ == "__main__":
    unittest.main()
