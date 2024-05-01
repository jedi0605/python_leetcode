"""_summary
1644. Lowest Common Ancestor of a Binary Tree IIDFS to search whole tree.
Solution1:
Find P Q are in the tree.
If not return None.
Else do regulare LCA search
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional
from TreeNode import TreeNode

# Solution2
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":        
        self.pFound = False
        self.qFound = False
        
        def postOrderDfs(root,p,q):
            if not root:
                return None
            l = postOrderDfs(root.left,p,q)
            r = postOrderDfs(root.right,p,q)
            
            if root.val == p.val or root.val == q.val:
                if root.val == p.val:
                    self.pFound = True
                else:
                    self.qFound = True
                return root
            if l and r:
                return root
            
            if l:
                return l
            else:
                return r
                 
        ans = postOrderDfs(root,p,q)        
        return ans if self.pFound and self.qFound else None
        
        
# Solution1
# class Solution:
#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":

#         self.findP = False
#         self.findQ = False

#         def findAllNode(root: "TreeNode", p: "TreeNode", q: "TreeNode"):
#             if not root:
#                 return None
#             if root.val == p.val:
#                 self.findP = True
#             if root.val == q.val:
#                 self.findQ = True
#             findAllNode(root.left, p, q)
#             findAllNode(root.right, p, q)

#         def LCA(root: "TreeNode", p: "TreeNode", q: "TreeNode"):
#             if not root:
#                 return None
#             if root.val == p.val or root.val == q.val:
#                 return root
#             lNode = LCA(root.left, p, q)
#             rNode = LCA(root.right, p, q)
#             if lNode and rNode:
#                 return root
#             if lNode:
#                 return lNode
#             else:
#                 return rNode

#         findAllNode(root, p, q)
#         if self.findP == False or self.findQ == False:
#             return None
#         return LCA(root, p, q)
