from collections import Counter, deque
import heapq
from typing import List

"""_summary_
LeetCode 323. Number of Connected Components in an Undirected Graph
Union find
T: O
S: O(1)
#Meta Tag
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # [0, 1, 2, 3, 4]
        # represnt each node it self.
        par = [0] * n
        for i in range(n):
            par[i] = i
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res-=union(n1, n2)
        return res
