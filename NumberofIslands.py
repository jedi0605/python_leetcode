"""_summary
Leetcode 200. Number of Islands
BFs search to travel all the r,c.
1. set to track visited.
2. BFS to find each island.
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.r, self.c = len(grid), len(grid[0])
        self.visited = set()
        island = 0

        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.bfsHelper(grid, i, j)
                    island += 1
        return island

    def bfsHelper(self, grid, i, j):
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        q.append((i, j))

        while q:
            row, col = q.popleft()
            for dr, dc in direction:
                subR, subC = row + dr, col + dc
                if (
                    (subR, subC) not in self.visited
                    and subR < self.r
                    and subR >= 0
                    and subC < self.c
                    and subC >= 0
                    and grid[subR][subC] == "1"
                ):
                    self.visited.add((subR, subC))
                    q.append((subR, subC))
