from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])  # sort by start position
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]  # get last end value

            if start <= lastEnd:  # equal, overlapping
                # [1, 5] [2, 4] => using max to get the end of merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
