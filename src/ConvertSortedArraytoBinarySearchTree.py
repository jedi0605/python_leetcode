"""_summary
Leetcode 108. Convert Sorted Array to Binary Search Tree

#Leetcode150
Time:O(n)
Space:O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            node.left = helper(left, middle - 1)
            node.right = helper(middle + 1, right)
            return node

        return helper(0, len(nums) - 1)
