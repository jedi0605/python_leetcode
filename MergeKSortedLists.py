"""_summary
23. Merge k Sorted Lists
#Leetcode150
Time:O(nlogn)
Space:O(1)
"""

from collections import deque, defaultdict
from typing import List, Optional

from ListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None

        while len(lists) > 1:
            mergeTmp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # Keep in the boundary
                mergeTmp.append(self.merge2Lists(l1, l2))
            lists = mergeTmp
        return lists[0]

    def merge2Lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return tail.next
