"""_summary
LeetCode 129. Sum Root to Leaf Numbers
Using Stack to track sum
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self._dfs(root, 0)

    def _dfs(self, root: TreeNode, val: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return val * 10 + root.val

        currL = self._dfs(root.left, val * 10 + root.val)
        currR = self._dfs(root.right, val * 10 + root.val)
        return currL + currR
