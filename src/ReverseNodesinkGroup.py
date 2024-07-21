"""_summary_
LeetCode 25. Reverse Nodes in k-Group
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import Optional
from ListNode import ListNode, Node


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dumm = ListNode(0)
        dumm.next = head
        groupPre = dumm

        while True:
            kth = self.getKth(groupPre, k)
            if kth == None:
                break
            groupNext = kth.next

            # k=2
            # pre
            #   1     2       3       4       5
            #   curr  kth
            #   1 should connext to 3
            # revers between groupPre <-> groupNext
            pre, curr = kth.next, groupPre.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp
            # tmp = curr
            # curr = curr.next
            # curr.next = tmp
            # pre = tmp

            # deal with groupPre.next
            tmp = groupPre.next
            groupPre.next = kth
            groupPre = tmp  # move groupPre to next one.
        return dumm.next

    def getKth(self, curr: ListNode, k: int) -> ListNode:
        while curr != None and k > 0:
            curr = curr.next
            k -= 1
        return curr
