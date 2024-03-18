"""_summary
Leetcode 207.Course Schedule

#Leetcode150
Time:O(n)
Space:O(n)
"""

import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses    0 1 2 3 4
        # indegree  [0,0,0,0,0]
        indegree = numCourses * [0]
        adj = collections.defaultdict(list)
        
        # [1,0] as prereq.
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])  # add node -> cource, 0 -> 1
            indegree[prereq[0]] += 1  # add indegree

        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        visit = 0  # our goul is visit every node one times
        while q:
            node = q.popleft()
            visit += 1
            for nei in adj[node]:
                indegree[nei] -= 1  # delete indegree
                if indegree[nei] == 0:
                    q.append(nei)
        return visit == numCourses
