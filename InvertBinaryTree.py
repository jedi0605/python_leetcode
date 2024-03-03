"""_summary
LeetCode 226. Invert Binary Tree
#Leetcode150
Time:O(n)
Space:O(1)
"""

from TreeNode import TreeNode
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self._invert(root)

    def _invert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self._invert(root.left)
        self._invert(root.right)
        return root
