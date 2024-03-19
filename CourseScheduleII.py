"""_summary
Leetcode 210.Course ScheduleII
Ref. https://www.youtube.com/watch?v=EUDwWbvtB_Q&ab_channel=AlgoEngine
#Leetcode150
Time:O(n)
Space:O(n)
"""

import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = numCourses * [0]
        maps = collections.defaultdict(list)
        for a,b in prerequisites:            
            indegree[a] += 1
            maps[b].append(a)

        q = collections.deque()

        # select 0 indegree elements
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        while q:
            cur = q.popleft()
            visited += 1
            res.append(cur)
            for i in maps[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return res if visited == numCourses else []
