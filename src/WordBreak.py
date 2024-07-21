"""_summary_
Leetcode 139. Word Break
Using backtracking or BFS also words
Time: m * N * N
SPACE: O(n)
"""

from collections import defaultdict, deque
import string
from typing import List


class Solution:
     # Queue ver
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        q = deque([s])
        visited = set()
        while q:
            word = q.popleft()

            if word in visited:
                continue
            else:
                if word == "":
                    return True
                visited.add(word)
                for start_word in wordDict:
                    if word.startswith(start_word):
                        q.append(word[len(start_word) :])
        return False
        # T : O(L) * O(N) * O(N)
    # Backtracking ver
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #     res = []
    #     memo = {}

    #     def helper(string: str):
    #         if string in memo:
    #             return memo[string]
    #         if not string:
    #             return [""]
    #         local = []
    #         for word in wordDict:
    #             if string.startswith(word):
    #                 subword = helper(string[len(word) :])

    #     return res
