"""_summary_
Leetcode 990. Satisfiability of Equality Equations
# Union find
#Leetcode150
"""

from typing import List

class UnionFind:
    def __init__(self):
        self.root = {}
        self.val = {}
    def _add(self,key):
        self.root[key] = key
        self.val[key] = 1
    def find(self,key):
        if key not in self.root:
            self._add(key)
        vals = 1
        while self.root[key] != key:
            key = self.root[key]
            vals *= self.val[key]
        
        


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        