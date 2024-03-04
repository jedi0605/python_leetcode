"""_summary
106. Construct Binary Tree from Inorder and Postorder Traversal
Last index in Postorder will be root.
#Leetcode150
Time:O(n)
Space:O(n)
"""

from TreeNode import TreeNode
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {}
        for i in range(len(inorder)):
            inorderIdx[inorder[i]] = i
        return self._helper(inorder, postorder, 0, len(inorder) - 1, inorderIdx)

    def _helper(
        self,
        inorder: List[int],
        postorder: List[int],
        L: int,
        R: int,
        inorderIdx: map,
    ):

        if L > R:
            return None

        root = TreeNode(postorder.pop())
        mid = inorderIdx[root.val]

        root.right = self._helper(inorder, postorder, mid + 1, R, inorderIdx)
        root.left = self._helper(inorder, postorder, L, mid - 1, inorderIdx)
        return root

    # V1 version O(N2), O(N2)
    #    if len(inorder) == 0:
    #         return None

    #     root = TreeNode(postorder.pop())
    #     mid = inorder.index(root.val)
    #     newInorderR = inorder[mid + 1 :]
    #     root.right = self.buildTree(newInorderR, postorder)

    #     newInorderL = inorder[:mid]
    #     root.left = self.buildTree(newInorderL, postorder)

    #     return root
