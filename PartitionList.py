"""_summary_
LeetCode 86. Partition List
Using L,R list to track value.
H   1   4   3   2   5   2
x = 3
if h<3 
L   1   2   2
else
R   4   3   5

Ltail.next = R
Rtail.next = None
  
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import Optional
from ListNode import ListNode, Node


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head != None:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = right.next
        rtail.next = None
        return left.next
