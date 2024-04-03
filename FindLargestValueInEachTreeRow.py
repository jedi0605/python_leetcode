from collections import deque
from typing import List, Optional

from TreeNode import TreeNode

"""_summary_
LeetCode 515. Find Largest Value in Each Tree Row
T: O(n)
S: O(n)
#Meta Tag
"""


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            count = len(q)
            levelMax = 0
            for i in range(count):
                curVal = q.popleft()
                levelMax = max(curVal.val, levelMax)
                if curVal.left != None:
                    q.append(curVal.left)
                if curVal.right != None:
                    q.append(curVal.right)
            res.append(levelMax)
        return res
