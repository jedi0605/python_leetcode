"""_summary
Leetcode 1161. Maximum Level Sum of a Binary Tree
BFS 
Time:O(n)
Space:O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

from TreeNode import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        level = 1
        max_val = float("-inf")
        max_level = 0
        q.append(root)

        while q:
            cnt = len(q)
            level_sum = 0
            for _ in range(cnt):
                cur = q.popleft()
                level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if level_sum > max_val:
                max_val = level_sum
                max_level = level

            level+=1
        return max_level