import unittest
from SimplifyPath import Solution


class test_ValidParentheses(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        path = "/home//foo/"
        assert solution.simplifyPath2(path) == "/home/foo"

if __name__ == "__main__":
    unittest.main()
