import math
from typing import List

"""_summary_
Leetcode 406. Queue Reconstruction by Height
Returns:
    _type_: _description_
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0], x[1]))
        print(people)
        res = []
        for a in people:
            res.insert(a[1],a)
        return res
