"""_summary
236. Lowest Common Ancestor of a Binary Tree
DFS to search whole tree.
Find Left, right side. if find left, right return curr node.
Else one of Left or right have value other is null. Have value's one is LCA
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        if l:
            return l
        else:
            return r
