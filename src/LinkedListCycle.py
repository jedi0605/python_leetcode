"""_summary_
LeetCode 141. Linked List Cycle
Using two pointer to solve.
Why is work.
In loop linked list, SlowPointer, FashPointer disten is 10
So every time move one step look like this:
Time1 : 10 + (1 - 2) = 9
Time2 : 9 + (1 -2) = 8 .....
So it will work at all.
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
