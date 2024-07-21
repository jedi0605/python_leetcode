import unittest
from IPO import Solution


class test_IsIsomorphic(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        k = 2
        w = 0
        profits = [1,2,3]
        capital = [0,1,1]
        
        assert solution.findMaximizedCapital(k,w,profits,capital) == 4



def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
