"""_summary
103. Binary Tree Zigzag Level Order Traversal
BFS. Travel each level. Setting a boolen to controll left->right or right->legt
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        while q:
            c = len(q)
            leverR = []
            for _ in range(c):
                curr = q.popleft()
                leverR.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if len(res) % 2 == 1:
                leverR = leverR[::-1]
            res.append(leverR)
        return res
