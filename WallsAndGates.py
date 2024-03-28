"""_summary_
Leetcode 286. Walls and Gates
Add gate to the queue. Do BFS at the same time.
Time: m * N * N
SPACE: O(n)
"""

from collections import defaultdict, deque
import string
from typing import List


class Solution:
    # Queue ver
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        visited = set()
        q = deque()

        def AddQueue(r, c):
            if (
                r >= 0
                and r < ROWS
                and c >= 0
                and c < COLS
                and rooms[r][c] != -1
                and (r, c) not in visited
            ):
                q.append((r, c))
                visited.add((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        step = 0
        while q:
            count = len(q)
            for i in range(count):
                r, c = q.popleft()
                rooms[r][c] = step
                AddQueue(r - 1, c)
                AddQueue(r + 1, c)
                AddQueue(r, c + 1)
                AddQueue(r, c - 1)

            step += 1
