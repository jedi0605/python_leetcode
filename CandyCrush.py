from collections import Counter, defaultdict, deque
import heapq
from typing import List

"""_summary_
LeetCode 723. Candy Crush
T: O
S: O(1)
#Meta Tag
"""


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])

        # find
        def find():
            crushed_set = set()
            # Check COLS
            for r in range(1, ROWS - 1):
                for c in range(COLS):
                    if board[r][c] == 0:
                        continue
                    if board[r - 1][c] == board[r][c] == board[r + 1][c]:
                        crushed_set.add((r, c))
                        crushed_set.add((r + 1, c))
                        crushed_set.add((r - 1, c))
            # Check ROWS
            for r in range(ROWS):
                for c in range(1, COLS - 1):
                    if board[r][c] == 0:
                        continue
                    if board[r][c - 1] == board[r][c] == board[r][c + 1]:
                        crushed_set.add((r, c))
                        crushed_set.add((r, c - 1))
                        crushed_set.add((r, c + 1))
            return crushed_set

        # crush (mark to zero)
        def crush(crush_set):
            for r, c in crush_set:
                board[r][c] = 0

        # drop
        def drop():
            for c in range(COLS):
                lowest_zero = -1
                for r in range(ROWS - 1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = (
                            board[lowest_zero][c],
                            board[r][c],
                        )
                        lowest_zero -= 1
                        
        crushed_set = find()
        while crushed_set:
            crush(crushed_set)
            drop()
            crushed_set = find()
        return board
