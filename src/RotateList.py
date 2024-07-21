"""_summary_
LeetCode 61. Rotate List
1. find length
2. k = k%length
                T
1   2   3   4   5
3. find new tail : length - k -1
        N       T
1   2   3   4   5
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import Optional
from ListNode import ListNode, Node


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        #
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head
        # move to new tail
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead
