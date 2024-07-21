"""_summary
LeetCode 104. Maximum Depth of Binary Tree
DFS search
#Leetcode150
Time:O(n)
Space:O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        return self._depth(root)

    def _depth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftVal = self._depth(root.left)
        rightVal = self._depth(root.right)
        return 1+ max(leftVal,rightVal)
