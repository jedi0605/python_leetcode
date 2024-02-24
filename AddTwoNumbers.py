"""_summary_
LeetCode 2. Add Two Numbers
Mention carry.
in the end if carry == 1. add new ListNode
#Leetcode150
Time:O(1)
Space:O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from typing import Optional
from ListNode import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        carry = 0
        dumm = ListNode(0)
        cur = dumm
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update pointer
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Edge case: 8 + 7
        if carry == 1:
            cur.next = ListNode(1)
        return dumm.next
