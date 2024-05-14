from collections import defaultdict
import collections
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        maps = {}
        # for i,val in enumerate(people):
        #     maps[val] = i
        people.sort()
        l, r = 0, len(people) - 1
        boat=0
        while l <= r:
            if people[l]+people[r] <= limit:
                l+=1
                r-=1
            else:
                r-=1
            boat+=1
        return boat
            
