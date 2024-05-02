"""_summary
1676. Lowest Common Ancestor of a Binary Tree IV
"""

from typing import List
from TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        # post order?
        self.NodeSet = set(nodes)

        def dfs(root):
            if not root:
                return None
            if root in nodes:
                return root
            l = dfs(root.left)
            r = dfs(root.right)

            if r and l:
                return root
            if l:
                return l
            else:
                return r

        return dfs(root)

