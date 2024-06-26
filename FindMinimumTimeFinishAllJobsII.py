"""_summary
2323. Find Minimum Time to Finish All Jobs II
"""

import math
from typing import List


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        res = 0
        for i in range(len(jobs)):
            job = jobs[i]
            worker = workers[i]
            time = math.ceil(job / worker)
            res = max(res, time)
        return res
