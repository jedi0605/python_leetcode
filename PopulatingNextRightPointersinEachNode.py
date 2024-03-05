"""_summary
LeetCode 116. Populating Next Right Pointers in Each Node
Setting Curr(1) and Nxt(2). like BFS trav.
        1
      2   3
    4  5 6  7  
curr.left.next = curr.right # base case.
if curr have next, deal with 2 connect to 3
    curr.right.next  = curr.next.left
curr = curr.next # curr from 2 move to 3
if curr == null
    # move to next layer
    

Inorder left side is tree left, other is right
#Leetcode150
Time:O(n)
Space:O(n)
"""

from TreeNode import TreeNode
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        curr = root
        next = curr.left if curr != None else None

        while curr != None and next != None:
            curr.left.next = curr.right
            if curr.next != None:
                curr.right.next = curr.next.left

            curr = curr.next

            if curr == None:  # move curr node to next level
                curr = next
                next = curr.left
        return root
