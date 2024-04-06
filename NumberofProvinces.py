from collections import Counter, deque
import heapq
from typing import List

"""_summary_
LeetCode 547. Number of Provinces
Union find
T: O
S: O(1)
#Meta Tag
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [0] * n
        rank = [1] * n
        for i in range(n):
            par[i] = i

        def find(n1):
            res = n1
            while res != par[res]:
                res = par[res]
            return res

        def Union(n1, n2):
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

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    n -= Union(i, j)
        return n
