"""_summary
1650. Lowest Common Ancestor of a Binary Tree III

Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# Solution2
# T:O(N) S:O(1)
class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        p_copy = p
        q_copy = q
        while p_copy != q_copy:
            p_copy = p_copy.parent if p_copy else q
            q_copy = q_copy.parent if q_copy else p
        return p_copy


# Solution1. T:O(N), S:O(N)
class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        while q:
            if q in seen:
                return q
            q = q.parent
        return None
