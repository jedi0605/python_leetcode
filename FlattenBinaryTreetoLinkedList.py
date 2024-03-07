"""_summary
LeetCode 114. Flatten Binary Tree to Linked List
V1. Using Stack to build flat tree. Time O(n) Space O(n)
V2. Using while loop. find each left tree's right most node. and re-connect to the tree
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                rightTail = curr.left
                while rightTail.right:
                    rightTail = rightTail.right  # find the right node of sub tree
                rightTail.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

        # With Stack
        # if root == None:
        #     return None
        # stack = []
        # stack.append(root)

        # while stack:
        #     curr = stack.pop()
        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)
        #     if len(stack) > 0:
        #         curr.right = stack[-1]
        #     curr.left = None
