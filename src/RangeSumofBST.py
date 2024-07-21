"""_summary_
Leetcode 938. Range Sum of BST
Using inorder, 
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0

        def inorder(node: TreeNode):
            if node == None:
                return
            inorder(node.left)
            
            if node.val >= low and node.val <= high:
                self.res += node.val
            inorder(node.right)
        inorder(root)
        return self.res
