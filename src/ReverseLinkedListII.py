"""_summary_
LeetCode 92. Reverse Linked List II
1. reach
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import Optional
from ListNode import ListNode, Node


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        preL = dummy
        curr = head
        # reach node at position "left"
        for i in range(left - 1):
            preL = curr
            curr = curr.next

        # Now cur="left", preL="node before left"
        # revers form left to right
        pre = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = pre
            pre = curr 
            curr = tmp             

        # complete final
        preL.next.next = curr
        preL.next = pre

        return dummy.next
