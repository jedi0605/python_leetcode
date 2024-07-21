"""_summary
LeetCode 173. Binary Search Tree Iterator
Every time append to array -> get all left side node.
Pop will check node have right side. if have right side, 
keep going left as far as we can adding each node to stack
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List, Optional

from TreeNode import TreeNode

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):        
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left
        
        
    def next(self) -> int:
        res =self.stack.pop()
        curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        
        return res.val

    def hasNext(self) -> bool:
        if  len(self.stack) > 0:
            return True
        return False