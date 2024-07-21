"""_summary
819. Most Common Word
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        for i in symbols:
            paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.lower().split()
        cnt = defaultdict(int)
        for s in paragraph:
            if s not in banned:
                cnt[s]+=1
        # max(cnt) default return key, add key=cnt.get. find max_value's key
        max_word = max(cnt, key=cnt.get)
        return max_word
    
        # manual parse paragraph
        # paragraph+="."
        # while i < len(paragraph):
        #     if paragraph[i].isalpha():
        #         tmp += paragraph[i].lower()
        #     else:
        #         if tmp in banned:
        #             tmp = ""
        #         if tmp != "":
        #             arr_tmp.append(tmp)
        #             tmp = ""
        #     i += 1