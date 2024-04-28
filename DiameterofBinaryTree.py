from collections import Counter, defaultdict, deque
from typing import List, Optional

from TreeNode import TreeNode

"""_summary_
LeetCode 759. Employee Free Time
T: O (nlog(n)) by sort
S: O(1)
#Meta Tag
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDia = 0

        def helper(node):
            if not node:
                return 0
            lSide = helper(node.left)
            rSide = helper(node.right)
            self.maxDia = max(self.maxDia, lSide + rSide)
            return 1 + max(lSide, rSide)

        helper(root)
        return self.maxDia
