"""_summary
230. Kth Smallest Element in a BST
Using DFS_inorder travel tree. and return num of k pop out
#Leetcode150
Time:O(n)
Space:O(n)
"""

from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0
        # do Inorder DFS
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
        return 0

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     self.arr = []
    #     self.inOrder(root)
    #     return self.arr[k - 1]

    # def inOrder(self, root: TreeNode):
    #     if not root:
    #         return
    #     self.inOrder(root.left)
    #     self.arr.append(root.val)
    #     self.inOrder(root.right)
