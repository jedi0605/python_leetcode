import unittest
from GasStation import Solution


class test_GasStation(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        res = solution.canCompleteCircuit(gas, cost)
        assert res == 3

    def test_case2(self):
        solution = Solution()
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        res = solution.canCompleteCircuit(gas, cost)
        assert res == -1


if __name__ == "__main__":
    unittest.main()
