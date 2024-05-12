import unittest
from ReorderDataLogFiles import Solution
from ListNode import ListNode
import TestingTool


class ReorderDataLogFiles_test(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        logs = [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
        res = solution.reorderLogFiles(logs)
        ans = [
            "let1 art can",
            "let3 art zero",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ]
        assert res == ans


if __name__ == "__main__":
    unittest.main()
