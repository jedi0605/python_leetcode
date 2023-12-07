import unittest
from ReverseWordsInAString import Solution


class test_ReverseWordsInAString(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        assert solution.reverseWords("the sky is blue") == "blue is sky the"
        assert solution.reverseWords("  hello world  ") == "world hello"
        assert solution.reverseWords("a good   example") == "example good a"

if __name__ == "__main__":
    unittest.main()
