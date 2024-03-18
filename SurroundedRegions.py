"""_summary
Leetcode 130. Surrounded Regions
1. Find the unsurrounded form edge. and do DFS search to mark all connected element to "T"
2. For loop to mark every "O" to "X"
3. For loop to mark every "T" to "O"
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.ROWS, self.COLS = len(board), len(board[0])
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O" and (
                    r in [0, self.ROWS - 1] or c in [0, self.COLS - 1]
                ):
                    self.dfsHelper(r, c, board)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

    def dfsHelper(self, r, c, board):
        if  r < 0 or c < 0 or r == self.ROWS or c == self.COLS or board[r][c] != "O":
            return
        board[r][c] = "T"
        self.dfsHelper(r + 1, c, board)
        self.dfsHelper(r - 1, c, board)
        self.dfsHelper(r, c + 1, board)
        self.dfsHelper(r, c - 1, board)
