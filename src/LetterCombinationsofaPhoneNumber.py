"""_summary_
Leetcode 17. Letter Combinations of a Phone Number
Backtracking recursive
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []
        self.backtrack(digits, 0, "")
        return self.res

    def backtrack(self, digits, idx, word) -> None:
        if len(digits) == len(word):
            self.res.append(word)
        else:
            for c in self.phone_map[digits[idx]]:
                self.backtrack(digits, idx + 1, word + c)
