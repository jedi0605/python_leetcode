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

import numpy as np
from TreeNode import TreeNode


class Union:
    def __init__(self, size: int):
        self.parent = [0] * size
        self.rank = [0] * size
        self.count = size
        for i in range(size):
            self.parent[i] = i

    def find(self, x: int):
        res = x
        while res != self.parent[res]:
            res = self.parent[res]
        return res

    def union(self, x: int, y: int):
        print(str(x) + "," + str(y))
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.rank[x] += 1
            self.parent[y] = x
        else:
            self.rank[y] += 1
            self.parent[x] = y
        self.count -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    count += 1
        # union find
        mn = len(grid) * len(grid[0])
        un = Union(mn)
        un.count = count
        nr = len(grid)
        nc = len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        un.union(r * nc + c, (r - 1) * nc + c)
                    if r + 1 < nr and grid[r + 1][c] == "1":
                        un.union(r * nc + c, (r + 1) * nc + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        un.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c + 1] == "1":
                        un.union(r * nc + c, r * nc + c + 1)
        return un.count

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return 0
    #     self.r, self.c = len(grid), len(grid[0])
    #     self.visited = set()
    #     island = 0

    #     for i in range(self.r):
    #         for j in range(self.c):
    #             if grid[i][j] == "1" and (i, j) not in self.visited:
    #                 self.bfsHelper(grid, i, j)
    #                 island += 1
    #     return island

    # def bfsHelper(self, grid, i, j):
    #     direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #     q = deque()
    #     q.append((i, j))

    #     while q:
    #         row, col = q.popleft()
    #         for dr, dc in direction:
    #             subR, subC = row + dr, col + dc
    #             if (
    #                 (subR, subC) not in self.visited
    #                 and subR < self.r
    #                 and subR >= 0
    #                 and subC < self.c
    #                 and subC >= 0
    #                 and grid[subR][subC] == "1"
    #             ):
    #                 self.visited.add((subR, subC))
    #                 q.append((subR, subC))
