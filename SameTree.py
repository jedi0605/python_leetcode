"""_summary
LeetCode 100. Same Tree
Recursive. Be careful with None case.
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        if self.isSameTree(p.left, q.left) == False:
            return False

        if self.isSameTree(p.right, q.right) == False:
            return False
        return p.val == q.val
