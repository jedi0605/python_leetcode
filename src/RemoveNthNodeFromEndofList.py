"""_summary_
LeetCode 19. Remove Nth Node From End of List
Using two pointer to located the nth node.
if nth=2
1   2   3   4   5
L       R
when R move to null. L will be nth
1   2   3   4   5   Null
            L       R
Next step is 3 link to 5. So we shit L to Dummy at the begin like:
D   1   2   3   4   5
            L           R
So L.next = L.next.next


#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import Optional
from ListNode import ListNode, Node


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumm = ListNode(0)
        dumm.next = head
        lN = dumm
        rN = dumm

        for i in range(n + 1):
            rN = rN.next

        while rN:  # rN != None will keep while loop
            rN = rN.next
            lN = lN.next

        lN.next = lN.next.next
        return dumm.next
