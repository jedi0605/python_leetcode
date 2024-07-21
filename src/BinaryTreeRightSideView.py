"""_summary
199. Binary Tree Right Side View
BFS travels the tree. Keep track at last tree node of each queue.
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)

        while q:
            c = len(q)            
            for i in range(c):
                curr = q.popleft()
                if i == 0:
                    res.append(curr.val)
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
                
        return res
