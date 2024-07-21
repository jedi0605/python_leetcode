import unittest
from NumberofConnectedComponentsinanUndirectedGraph import Solution


class test_NumbersOfIslands(unittest.TestCase):
    def test_case1(self):
        n = 5
        edges = [[0,1],[1,2],[3,4]]
        sol = Solution()
        
        assert sol.countComponents(n,edges) == 2


if __name__ == "__main__":
    unittest.main()
