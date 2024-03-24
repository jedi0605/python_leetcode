"""_summary_
Leetcode 212. Word Search II
Using prefix tree(Trie DS) and WordSearch
Word Search is using backtracking dfs.
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


class TrieNode:
    def __init__(self) -> None:
        self.children = {}  # key Char. valuse is TrieNode
        self.wordEnd = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.wordEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        # Create Trie (M * N)
        for w in words:
            self.root.addWord(w)

        self.ROW, self.COL = len(board), len(board[0])
        self.res, self.visited = set(), set()
        for r in range(self.ROW):
            for c in range(self.COL):
                self.dfs(r, c, self.root, board, "")
        return list(self.res)

    def dfs(self, i: int, j: int, node: TrieNode, board: List[List[str]], word: str):
        if (
            i < 0
            or j < 0
            or i == self.ROW
            or j == self.COL
            or board[i][j] not in node.children
        ):
            return False

        self.visited.add((i, j))
        node = node.children[board[i][j]]
        word += board[i][j]
        if node.wordEnd:
            self.res.add(word)
        self.dfs(i + 1, j, node, board, word)
        self.dfs(i - 1, j, node, board, word)
        self.dfs(i, j + 1, node, board, word)
        self.dfs(i, j - 1, node, board, word)
        self.visited.remove((i, j))
