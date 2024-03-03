"""_summary
LeetCode 101. Symmetric Tree
Recursive. Be careful with None case.
#Leetcode150
Time:O(n)
Space:O(n)
"""

from TreeNode import TreeNode
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._dfs(root.left, root.right)

    def _dfs(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False

        #      1
        #    2   2  <- like this layer
        #   3 4 4 3
        return (
            left.val == right.val
            and self._dfs(left.left, right.right)
            and self._dfs(left.right, right.left)
        )
