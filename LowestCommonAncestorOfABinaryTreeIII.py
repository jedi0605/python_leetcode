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


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# Solution2
#
class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        p_copy = p
        q_copy = q
        while p_copy != q_copy:
            p_copy = p_copy.parent if p_copy else q
            q_copy = q_copy.parent if q_copy else p
        return p_copy


# Solution1. T:O(N), S:O(N)
class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        while q:
            if q in seen:
                return q
            q = q.parent
        return None


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
