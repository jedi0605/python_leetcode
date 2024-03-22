"""_summary_
Leetcode 127. Word Ladder
Must optimize the maps to increase the time complexted.
hot -> *ot, h*t, ho* to the map
step1. looks like:
wordList = ["hot","dot","dog","lot","log","cog"]
change_map ={ *ot : hot, dot, lot
			h*t : hot
			ho* :hot
			d*t : dot
			do* : dot, dog
			*og : dog, log, cog
			d*g : dog
			l*t : lot
			lo* : lot, log
			l*g : log
			c*g: cog
			co* : cog 
			}
Using BFS to find the shortest path
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import defaultdict, deque
import string
from typing import List

class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0
        maps = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for s in range(L):
                maps[word[:s] + "*" + word[s + 1 :]].append(word)
        q = deque()
        q.append([beginWord, 1])
        visist = set()
        visist.add(beginWord)
        while q:
            cur, steps = q.popleft()
            # list all combo of cur word => hot -> *ot, h*t, ho*
            for i in range(L):
                newWord = cur[:i] + "*" + cur[i + 1 :]
                for word in maps[newWord]:
                    if word == endWord:
                        return steps + 1
                    if word not in visist:
                        visist.add(word)
                        q.append([word, steps + 1])
        return 0

    # """
    # It's brust force ver. It will time out.
    # n: len(beginWord) b:len(wordList)
    # O: n( 26^n * b)
    # """
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     if endWord not in wordList:
    #         return 0
    #     q = deque()
    #     L = len(beginWord)

    #     q.append([beginWord, 1])
    #     while q:
    #         word, steps = q.popleft()
    #         if word == endWord:
    #             return steps
    #         # list all combo of hit. a-z: a-it, b-it, c-it etc..
    #         for i in range(L):
    #             for chr in string.ascii_lowercase:
    #                 newWord = word[:i] + chr + word[i + 1 :]
    #                 if newWord in wordList:
    #                     q.append([newWord, steps + 1])
    #                     wordList.remove(newWord)
    #     return 0
