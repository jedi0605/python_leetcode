"""_summary
LeetCode 124. Binary Tree Maximum Path Sum
Using postorder dfs. Remind nagtive number shoud return 0
calculate local subtree max value.
return max of LeftTree+curr or RightTree+curr
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    
    def __init__(self):
        self.global_var = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.global_var

    def postorder(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = max(self.postorder(root.left), 0)
        right = max(self.postorder(root.right), 0)
        self.global_var = max(self.global_var, root.val + left + right)
        return max(left + root.val, right + root.val)
