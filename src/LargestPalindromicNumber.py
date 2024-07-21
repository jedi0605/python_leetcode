from collections import Counter
import random
from typing import List

"""_summary_
LeetCode 2384. Largest Palindromic Number
"""


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        first_part = ""
        center = -1

        for i in range(9, -1, -1):
            char = str(i)
            if char in count:
                if count[char] >= 2:
                    first_part += str(i) * (count[char] // 2)
                if count[char] % 2 == 1:
                    center = max(center, i)
        first_part = first_part.lstrip("0")
        mid_str = str(center) if center >= 0 else ""
        res = first_part + mid_str + first_part[::-1]
        return res if res != "" else "0"

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
