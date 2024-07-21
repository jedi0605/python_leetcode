from collections import Counter, defaultdict, deque
import heapq
from typing import List

"""_summary_
LeetCode 721. Accounts Merge
Union find
T: O
S: O(1)
#Meta Tag
"""


class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [0] * n
        self.rank = [1] * n
        for i in range(n):
            self.par[i] = i

    def find(self, n1):
        res = n1
        while res != self.par[res]:
            res = self.par[res]
        return res

    def Union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        un = UnionFind(len(accounts))
        mailToAcc = {}  # mail-> idx of acc

        # mail -> idx of acc map
        # and union group
        for idx, a in enumerate(accounts):
            for e in a[1:]:
                if e in mailToAcc:
                    parIdx = mailToAcc[e]
                    un.Union(parIdx, idx)
                else:
                    mailToAcc[e] = idx

        # build acc -> emails
        # group will like 0:[e1,e2] 1:[e3]
        emailGroup = defaultdict(list)  # idx of account to mailList

        for mail, accIdx in mailToAcc.items():
            rootP = un.find(accIdx)
            emailGroup[rootP].append(mail)

        # build res
        res = []
        for key, values in emailGroup.items():
            name = accounts[key][0]
            res.append([name] + sorted(values))
        return res
