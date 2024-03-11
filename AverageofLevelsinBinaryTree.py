"""_summary
637. Average of Levels in Binary Tree
BFS. Travel each level
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)

        while q:
            c = len(q)
            avg = 0
            for i in range(c):
                curr = q.popleft()
                avg += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(avg / c)
        return res
