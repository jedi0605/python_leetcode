"""_summary
102. Binary Tree Level Order Traversal
BFS. Travel each level
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        
        while q:
            c = len(q)
            levelArr = []
            for _ in range(c):
                curr = q.popleft()
                levelArr.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(levelArr)
        return res