from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:  # new interval is before i interval
                res.append(newInterval)                
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:  # new interval is after i interval
                res.append(intervals[i])
            else:  
                # overlapping, do not add right away. 
                # maybe the end of interval is overlapping next one.
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
            # edge case. newInterval is the end of List.
        res.append(newInterval)
        return res
