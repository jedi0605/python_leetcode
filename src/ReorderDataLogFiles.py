from collections import Counter, defaultdict
import collections
from typing import List

"""_summary
LeetCode 937. Reorder Data in Log Files

#Leetcode150
Time:O(n)
Space:O(n)
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # split digi or letter log
        # if digit log. Just append
        digLog = []
        # if letter log. create a stuct (val,key,idx)
        letterLog = []

        for l in logs:
            if l[-1].isdigit():
                digLog.append(l)
            else:
                letterLog.append(l)
        letterLog.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        # letterLog.sort(key=lambda x: )
        
        return letterLog + digLog
    
        # digLog = []
        # # if letter log. create a stuct (val,key,idx)
        # letterLog = []
        # res = []

        # for i, l in enumerate(logs):
        #     if l[-1].isdigit():
        #         digLog.append(l)
        #     else:
        #         data = l.split(" ")
        #         key = data[0]
        #         vals = " ".join(data[1:])
        #         letterLog.append([vals, key, i])
        # letterLog = sorted(letterLog, key=lambda letter: (letter[0], letter[1]))
        # for l in letterLog:
        #     res.append(logs[l[2]])
        # return res + digLog
