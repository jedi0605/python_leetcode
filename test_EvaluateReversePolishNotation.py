import unittest
from EvaluateReversePolishNotation import Solution


class test_EvaluateReversePolishNotation(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        token = ["2", "1", "+", "3", "*"]
        assert solution.evalRPN(token) == 9
        token = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        res = solution.evalRPN(token)
        assert res == 22


if __name__ == "__main__":
    unittest.main()
