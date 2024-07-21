"""_summary
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
Preorder index 0 must be root, than find in Inorder.index(preorder[0])
Inorder left side is tree left, other is right
#Leetcode150
Time:O(n)
Space:O(n)
"""

from TreeNode import TreeNode
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        newPreLeft = preorder[1 : mid + 1]
        newInLeft = inorder[:mid]
        root.left = self.buildTree(newPreLeft, newInLeft)

        newPreRight = preorder[1 + mid :]
        newInRight = inorder[mid + 1 :]
        root.right = self.buildTree(newPreRight, newInRight)
        return root
