import unittest
from SatisfiabilityEqualityEquations import Solution


class SatisfiabilityEqualityEquations_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        equations = ["a==b","e==c","b==c","a!=e"]
        assert sol.equationsPossible(equations) == False


if __name__ == "__main__":
    unittest.main()
