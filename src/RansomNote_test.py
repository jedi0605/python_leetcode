import unittest
from RansomNote import Solution


class test_RansomNote(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        ransomNote = "aa"
        magazine = "aab"
        assert solution.canConstruct(ransomNote, magazine) == True

    def test_case2(self):
        solution = Solution()
        ransomNote = "aac"
        magazine = "aab"
        assert solution.canConstruct(ransomNote, magazine) == False


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
