"""_summary
LeetCode 117. Populating Next Right Pointers in Each Node II
BFS search. two pointer pre, curr if pre!=null pre.next = curr
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from TreeNode import TreeNode
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root
        q = deque([root])

        while q:
            pre = None
            for i in range(len(q)):
                curr = q.popleft()
                if pre:
                    pre.next = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                pre = curr
        return root