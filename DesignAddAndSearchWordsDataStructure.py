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


class TrieNode:
    def __init__(self) -> None:
        self.childern = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.childern:
                cur.childern[c] = TrieNode()
            cur = cur.childern[c]
        cur.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(word, curr)

    def dfs(self, word: str, root: TrieNode) -> bool:
        curr = root
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for sub in curr.childern.values():
                    if self.dfs(word[i + 1 :], sub):
                        return True
                return False
            else:
                if c not in curr.childern:
                    return False
                curr = curr.childern[c]

        return curr.word
