import unittest
from WordLadder import Solution


class WordLadder_test(unittest.TestCase):
    def test_case1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        solution = Solution()
        assert solution.ladderLength(beginWord, endWord, wordList) == 5


def are_matrices_equal(matrix1, matrix2):
    return all(row1 == row2 for row1, row2 in zip(matrix1, matrix2))


if __name__ == "__main__":
    unittest.main()
