"""_summary
98. Validate Binary Search Tree
1.Using DFS_inorder travel tree. Condition is  pre node value smaller than current node
2.Dfs to setting left, right side to compare with root.val
#Leetcode150
Time:O(n)
Space:O(n)
"""

from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.dfsInorder(root)
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, root: TreeNode, left, right) -> bool:
        if not root:
            return True
        if not (left < root.val and root.val < right):
            return False

        return self.valid(root.left, left, root.val) and self.valid(
            root.right, root.val, right
        )

    # def isValidBST_Stack(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return False
    #     stack = []
    #     pre = None
    #     curr = root
    #     while curr or stack:
    #         while curr:
    #             stack.append(curr)
    #             curr = curr.left
    #         curr = stack.pop()
    #         if pre != None and pre.val >= curr.val:
    #             return False
    #         pre = curr
    #         curr = curr.right
    #     return True
