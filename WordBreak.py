"""_summary_
Leetcode 212 - WordSearch
Using dfs backtracking 
#Leetcode150
Time: m* N * 4^l
l = word length
Search: O 4^l
Board: m*n
Space:O(m*n)
"""

from collections import defaultdict, deque
import string
from typing import List


class Solution:
    """DFS version. will time out."""

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def help(idx) -> bool:
            print(idx)
            if idx == len(s):
                return True
            if idx in memo:
                return memo[idx]

            for word in wordDict:
                wordL = len(word)
                subS = s[idx : idx + wordL]
                print(subS)
                if subS == word and help(idx + wordL):
                    memo[idx] = True
                    return True
            memo[idx] = False
            return False

        return help(0)
