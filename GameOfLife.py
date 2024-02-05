from typing import List

"""_summary_
Returns:
    _type_: _description_
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1 -> live if nei == 2,3 else die
        # 0 -> live if nei == 3 else die

        # Original | New | State
        #    0       0      0
        #    1       0      1
        #    0       1      2
        #    1       1      3
        def checkNeighbors(board: List[List[int]], r: int, c: int):
            row = len(board)
            col = len(board[0])
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i < 0 or j < 0 or i == row or j == col or (i == r and j == c):
                        continue
                    if board[i][j] == 1 or board[i][j] == 3:
                        nei += 1
            return nei

        row = len(board)
        col = len(board[0])
        # tmpBoard = []
        # for r in range(row):
        #     tmpBoard.append([])
        #     for c in range(col):
        #         tmpBoard[r].append(0)

        for r in range(row):
            for c in range(col):
                nei = checkNeighbors(board, r, c)
                if board[r][c]:  # ==1
                    if nei in [2, 3]:
                        board[r][c] = 3
                else:
                    if nei == 3:
                        board[r][c] = 2
        # Map the status
        for r in range(row):
            for c in range(col):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1

        print(board)
