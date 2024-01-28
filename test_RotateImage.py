import unittest
from RotateImage import Solution


class test_RotateImage(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        ans = [[7,4,1],[8,5,2],[9,6,3]]
        solution.rotate(matrix)
        self.assertTrue(are_matrices_equal(matrix, ans))
    
    def test_case2(self):
        solution = Solution()
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]        
        ans = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        solution.rotate(matrix)
        self.assertTrue(are_matrices_equal(matrix, ans))

def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))

if __name__ == "__main__":
    unittest.main()
