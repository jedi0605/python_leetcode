import unittest
from SetMatrixZeroes import Solution


class test_SetMatrixZeroes(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        solution.setZeroes(matrix)
        ans = [[1,0,1],[0,0,0],[1,0,1]]
        self.assertTrue(are_matrices_equal(matrix, ans))
        
    def test_case2(self):
        solution = Solution()
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        solution.setZeroes2(matrix)
        ans = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        self.assertTrue(are_matrices_equal(matrix, ans))
    
def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))

if __name__ == "__main__":
    unittest.main()
