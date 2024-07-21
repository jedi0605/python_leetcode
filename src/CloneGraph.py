"""_summary
Leetcode 133. Clone Graph

#Leetcode150
Time:O(n)
Space:O(n)
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import List, Optional
from TreeNode import TreeNode


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # oldToNew = {}

        # def dfs(node:Node):
        #     if node in oldToNew:
        #         return oldToNew[node]
        #     copy = Node(node.val)
        #     oldToNew[node] = copy
        #     for nie in node.neighbors:
        #         n = dfs(nie)
        #         copy.neighbors.append(n)
        #     return copy
        # return dfs(node) if node else None
        if not node:
            return None

        cloned = {}
        cloned[node] = Node(node.val, [])
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in cloned:
                    cloned[nei] = Node(nei.val)
                    q.append(nei)  ##  Add "curr" neighbors
                cloned[cur].neighbors.append(cloned[nei])
        return cloned[node]
