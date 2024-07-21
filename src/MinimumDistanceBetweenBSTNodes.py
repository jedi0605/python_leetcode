"""_summary
783. Minimum Distance Between BST Nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

from TreeNode import TreeNode


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min = float("inf")
        self.preNode = None

        def dfs_pre(node):
            if not node:
                return
            dfs_pre(node.left)
            if self.preNode:
                print(f"{node.val} - {self.preNode.val}")
                self.min = min(self.min, node.val - self.preNode.val)
            self.preNode = node
            dfs_pre(node.right)

        dfs_pre(root)
        return self.min
