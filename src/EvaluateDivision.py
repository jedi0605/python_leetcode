"""_summary
Leetcode 399. Evaluate Division

#Leetcode150
Time:O(n)
Space:O(n)
"""

import collections
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        self.adj = collections.defaultdict(list)  # Map a -> list of [b, a/b value]
        res = []
        for i, eq in enumerate(equations):
            a, b = eq
            self.adj[a].append([b, values[i]])
            self.adj[b].append([a, 1 / values[i]])

        for a, b in queries:
            res.append(self.bfsHelp(a, b))
        return res

    def bfsHelp(self, src, target) -> float:
        if src not in self.adj or target not in self.adj:
            return -1
        q = collections.deque()
        visit = set()  # not visit again
        q.append([src, 1])  # a -> a is 1
        visit.add(src)
        while q:
            num, w = q.popleft()
            if num == target:
                return w
            for nei, weight in self.adj[num]:
                if nei not in visit:
                    q.append([nei, w * weight])
                    visit.add(nei)
        return -1
