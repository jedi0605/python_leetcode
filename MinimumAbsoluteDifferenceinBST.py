"""_summary
530. Minimum Absolute Difference in BST
BFS. Travel each level.Using inorder , set pre node. abs(pre - curr)
#Leetcode150
Time:O(n)
Space:O(n)
"""

from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float("inf")
        self.pre = None
        self.inOrder(root)
        return self.min

    def inOrder(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        l = self.inOrder(root.left)
        if self.pre:
            self.min = min(self.min, abs(self.pre.val - root.val))
        self.pre = root
        r = self.inOrder(root.right)
