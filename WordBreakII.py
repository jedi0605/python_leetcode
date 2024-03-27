"""_summary_
Leetcode 140. Word Break II
BFS
#Leetcode150
Time: O(n^3)
Space:O(n)
"""

from collections import defaultdict, deque
import string
from typing import List


class Solution:

    # Queue ver
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        class wordRes:
            def __init__(self, string: str, res=[]):
                self.string = string
                self.res = res

        start = wordRes(s, [])
        q = deque([start])
        res = []
        while q:
            currNode = q.popleft()

            if currNode.string == "":
                res.append(" ".join(currNode.res))
            for start_word in wordDict:
                if currNode.string.startswith(start_word):
                    newNode = wordRes(
                        currNode.string[len(start_word) :], currNode.res + [start_word]
                    )
                    q.append(newNode)
        return res

        # queue = collections.deque( [(s, [])] )
        # res = []

        # while queue:
        #     word, cur_res = queue.popleft()
        #     if not word:
        #         res.append(" ".join(cur_res))
        #     for start in wordDict:
        #         if word.startswith(start):
        #             queue.append( (word[len(start):], cur_res + [start]) )
        # return res
