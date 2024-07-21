"""_summary_
LeetCode 21. Merge Two Sorted Lists
No need extra memory, remember add non null list to res
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
from ListNode import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dumm = ListNode(0)
        res = dumm

        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            res = res.next

        # left case will be L1 == null. L2==null. L1 L2 == null
        if list1 != None:
            res.next = list1
        else:
            res.next = list2

        return dumm.next
