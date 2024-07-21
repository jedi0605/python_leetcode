from bisect import bisect_left
import collections
import random
from typing import List

"""_summary_
LeetCode 381. Insert Delete GetRandom O(1) - Duplicates allowed
Using Maps{val: set()} , arr[]
#Leetcode150
Time:O(n^2)
Space:O(n)
"""

class RandomizedCollection:

    def __init__(self):
        self.maps = collections.defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        self.maps[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.maps[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.maps[val]:
            return False
        ridx = self.maps[val].pop()
        last_val = self.arr[-1]

        self.arr[ridx] = last_val # Swape the remove_val & last_val
        self.maps[last_val].add(ridx)
        self.maps[last_val].discard(len(self.arr) - 1)

        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
