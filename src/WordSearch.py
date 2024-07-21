"""_summary_
Leetcode 212 - WordSearch
Using dfs backtracking 
#Leetcode150
Time: m* N * 4^l
l = word length
Search: O 4^l
Board: m*n
Space:O(m*n)
"""

from collections import defaultdict, deque
import string
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                if self.dfsSearch(r, c, board, word, 0):
                    return True
        return False

    def dfsSearch(self, i, j, board, word, idx):
        # check bound, check match
        row = len(board)
        col = len(board[0])
        if i < 0 or j < 0 or i == row or j == col or board[i][j] != word[idx]:
            return False

        # check word completed
        if idx == len(word) - 1:
            return True
        tmpChar = board[i][j]
        board[i][j] = "0"
        found = (
            self.dfsSearch(i + 1, j, board, word, idx + 1)
            or self.dfsSearch(i - 1, j, board, word, idx + 1)
            or self.dfsSearch(i, j + 1, board, word, idx + 1)
            or self.dfsSearch(i, j - 1, board, word, idx + 1)
        )
        board[i][j] = tmpChar
        return found
