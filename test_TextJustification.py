import unittest
from TextJustification import Solution


class test_TextJustification(unittest.TestCase):
    def test_case1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]

        solution = Solution()
        res = solution.fullJustify(words, 16)
        ans = ["This    is    an", "example  of text", "justification.  "]
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
