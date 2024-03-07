"""_summary
LeetCode 117. Populating Next Right Pointers in Each Node II
BFS search. two pointer pre, curr if pre!=null pre.next = curr
Using O(n) O(n)
For mem O(1)
dummy, tmp to track each level head
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
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

    @staticmethod
    def array_to_binary_tree(arr, index=0):
        if index < len(arr):
            if arr[index] is None:
                return None
            root = Node(arr[index])
            root.left = Node.array_to_binary_tree(arr, 2 * index + 1)
            root.right = Node.array_to_binary_tree(arr, 2 * index + 2)
            return root
        return None


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        dummy = Node(-1, None, None, None)
        
        tmp = dummy
        res = root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next
            tmp = dummy
            dummy.next = None

        return res

        # def connect(self, root: "Node") -> "Node":
        # if not root:
        #     return root
        # q = deque([root])

        # while q:
        #     pre = None
        #     for i in range(len(q)):
        #         curr = q.popleft()
        #         if pre:
        #             pre.next = curr
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        #         pre = curr
        # return root
