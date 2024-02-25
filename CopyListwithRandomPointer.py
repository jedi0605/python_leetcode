"""_summary_
LeetCode 138. Copy List with Random Pointer
Using hashmap.
First loop to store old <->deepCopy
Second loop  set deepCopy.next random as same as old.next and old.random
#Leetcode150
Time:O(n)
Space:O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from ListNode import ListNode, Node


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        maps = {None: None}
        cur = head

        while cur is not None:
            copy = Node(cur.val)
            maps[cur] = copy
            cur = cur.next

        cur = head
        while cur is not None:
            copy = maps[cur]
            copy.next = maps[cur.next]
            copy.random = maps[cur.random]
            cur = cur.next

        return maps[head]
