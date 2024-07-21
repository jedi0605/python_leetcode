from collections import Counter, deque
import heapq
from typing import List

"""_summary_
LeetCode 621. Task Scheduler
T: O(n * m) # A,A,A * N
S: O(1)
#Meta Tag
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = []
        for cnt in count.values():
            maxHeap.append(-cnt)
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # [-cnt, idelTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:  # check idle time
                heapq.heappush(maxHeap, q.popleft()[0])            
        return time