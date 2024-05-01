"""_summary
235. Lowest Common Ancestor of a Binary Search Tree
DFS to search whole tree.
Find Left, right side. if find left, right return curr node.
Else one of Left or right have value other is null. Have value's one is LCA

#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        pV = p.val
        qV = q.val
        rV = root.val
        if rV > pV and rV>qV:
            return self.lowestCommonAncestor(root.left,p,q)
        elif rV<pV and rV<qV:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        