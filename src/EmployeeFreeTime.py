from collections import Counter, defaultdict, deque
from typing import List

"""_summary_
LeetCode 759. Employee Free Time
T: O (nlog(n)) by sort
S: O(1)
#Meta Tag
"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        events = []
        for employee in schedule:
            for event in employee:
                events.append(event)
        events.sort(key=lambda x: x.start)
        res = []
        last_max_end_time = events[0].end
        for interval in events:
            if interval.start <= last_max_end_time:
                last_max_end_time = max(interval.end, last_max_end_time)
                continue
            if interval.start > last_max_end_time:
                res.append(Interval(last_max_end_time, interval.start))
                last_max_end_time = interval.end
        return res
