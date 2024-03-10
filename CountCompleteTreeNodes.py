"""_summary
LeetCode 222. Count Complete Tree Nodes
DFS , BFS can do in O(n) time.
IF want to less than O(n)
Find sub complete binary tree and using 2^n - 1
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l = self.leftH(root)
        r = self.rightH(root)
        if l == r:
            return 2**l - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def leftH(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.leftH(root.left) + 1

    def rightH(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.rightH(root.right) + 1

        # BFS Ver.
        # res = 0
        # q= deque()
        # q.append(root)
        # while len(q) > 0:
        #     c = len(q)
        #     res+=c
        #     for _ in range(c):
        #         curr =  q.popleft()
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        # return res
