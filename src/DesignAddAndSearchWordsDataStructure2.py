"""_summary_
211. Design Add and Search Words Data Structure
Trie node??

#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import defaultdict, deque
import string
from typing import List


class WordDictionary:

    def __init__(self):
        self.maps = defaultdict(list)

    def addWord(self, word: str) -> None:
        l = len(word)
        self.maps[l].append(word)

    def search(self, word: str) -> bool:
        l = len(word)
        for m in self.maps[l]:
            idx = 0
            while idx < l and (word[idx] == "." or word[idx] == m[idx]):
                idx += 1
            if idx == l:
                return True
        return False
