"""_summary_
Leetcode 909. Snakes and Ladders
Using BFS to find the shortest path
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.length = len(board)
        board.reverse()
        q = deque()
        q.append([1, 0])  # square, moves
        visit = set()
        while q:
            square, moves = q.popleft()
            # run 1-6 step
            for i in range(1, 7):
                nextSquare = square + i
                r, c = self.intToPos(nextSquare)
                if board[r][c] != -1:  # special case
                    nextSquare = board[r][c]
                if nextSquare == self.length * self.length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1

    def intToPos(self, square):
        r = (square - 1) // self.length
        c = (square - 1) % self.length
        if r % 2 == 1:
            c = self.length - 1 - c
        return [r, c]
