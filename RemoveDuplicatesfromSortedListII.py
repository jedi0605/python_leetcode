"""_summary_
LeetCode 82. Remove Duplicates from Sorted List II
Two pointer approch
D   1   2   3   3   4   4   5
p   c
if c!=c.next
    move both
D   1   2   3   3   4   4   5
        p   c
if c==c.next
    c move
D   1   2   3   3   4   4   5
        p       c
if c!=c.next && p.next!=c.next
    p.next = c.next
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import Optional
from ListNode import ListNode, Node


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumm = ListNode(0)
        dumm.next = head
        pre = dumm
        curr = head

        while curr:
            if curr.next != None and curr.val == curr.next.val:
                # D   1   2   3   3   4   4   5
                #         p                   c
                while curr.next != None and curr.next.val == curr.val:
                    curr = curr.next
                pre.next = curr.next  # p->4, p->5
            else:
                pre = pre.next
            curr = curr.next
        return dumm.next
