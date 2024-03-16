import unittest
from LinkedListCycle import Solution
from ListNode import ListNode


class test_LinkedListCycle(unittest.TestCase):
    def test_case1(self):
        solution = Solution()

        # Example usage:
        nums = [3, 2, 0, -4]
        head = create_linked_list_with_cycle(nums, 1)
        assert solution.hasCycle(head) == True


def create_linked_list_with_cycle(nums, pos):
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head
    cycle_start = None

    for i, num in enumerate(nums[1:]):
        current.next = ListNode(num)
        current = current.next
        if i == pos - 1:
            cycle_start = current

    # Connect the last node to the node at position 'pos'
    if cycle_start:
        current.next = cycle_start

    return head


if __name__ == "__main__":
    unittest.main()
