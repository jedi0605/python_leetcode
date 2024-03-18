import unittest
from EvaluateDivision import Solution


class EvaluateDivision_test(unittest.TestCase):
    def test_case1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        sol = Solution()
        res = sol.calcEquation(equations, values, queries)
        ans = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        self.assertEqual(res, ans)
        
    def test_case2(self):
        equations = [["a","b"],["b","c"],["a","c"],["d","e"]]
        values = [2.0,3.0,6.0,1.0]
        queries = [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","d"]]
        sol = Solution()
        res = sol.calcEquation(equations, values, queries)
        ans = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()
