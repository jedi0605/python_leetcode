from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        arr = s.split(" ")
        return len(arr[-1])
