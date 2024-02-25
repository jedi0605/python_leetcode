# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def array_to_linked_list(nums):
        if not nums:
            return None

        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next

        return head

    @staticmethod
    def are_linked_lists_equal(head1, head2):
        # Traverse both linked lists simultaneously
        while head1 is not None and head2 is not None:
            # If values of corresponding nodes are not equal, lists are not equal
            if head1.val != head2.val:
                return False
            # Move to the next nodes
            head1 = head1.next
            head2 = head2.next
        return True
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random