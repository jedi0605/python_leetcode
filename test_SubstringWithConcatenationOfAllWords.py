import unittest
from SubstringWithConcatenationOfAllWords import Solution


class test_SubstringWithConcatenationOfAllWords(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        res = solution.findSubstring(s, words)
        ans = [0,9]
        self.assertEqual(res,ans)        



if __name__ == "__main__":
    unittest.main()
