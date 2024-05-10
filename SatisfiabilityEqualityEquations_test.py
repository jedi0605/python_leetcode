import unittest
from SatisfiabilityEqualityEquations import Solution


class SatisfiabilityEqualityEquations_test(unittest.TestCase):
    def test_case1(self):
        sol = Solution()
        equations = ["a==b","b!=a"]
        assert sol.equationsPossible(equations) == False


if __name__ == "__main__":
    unittest.main()
