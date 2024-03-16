import unittest
from ValidParentheses import Solution


class test_ValidParentheses(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        s = "()[]{}"
        assert solution.isValid(s) == True

if __name__ == "__main__":
    unittest.main()
