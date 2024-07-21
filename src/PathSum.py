"""_summary
LeetCode 112. Path Sum
V1. Using Stack to track sum
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._dfs(root, targetSum, 0)

    def _dfs(self, root: TreeNode, targetSum, curSum):
        if root == None:
            return False

        curSum += root.val
        if root.left == None and root.right == None:
            return curSum == targetSum

        resLeft = self._dfs(root.left, targetSum, curSum)
        resRight = self._dfs(root.right, targetSum, curSum)

        return resLeft or resRight
