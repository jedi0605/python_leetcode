"""_summary_
LeetCode 146. LRU Cache

HashMap => {KEY, Node}
Node => key,val, preNode, nextNode
LeftNode, RightNode = LeastUsed, RecentlyUsed
1. add func "remove" "insert"
    remove: remove form between node.
    insert: alway insert to right.
2. imprement get, put
    get: remove->insert
    put: if in cache:remove. insert(node)
        if over cap. remove Left.next from list and HashMap
#Leetcode150
Time:O(n)
Space:O(1)
"""

from typing import Optional


class DoubleNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.pre = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.LeftNode = DoubleNode(0, 0)
        self.RightNode = DoubleNode(0, 0)
        # link left right
        self.LeftNode.next = self.RightNode
        self.RightNode.pre = self.LeftNode
        self.cache = {}

    def printNodes(self):
        dumm = self.LeftNode
        while dumm:
            print(dumm.val, end=" ")
            dumm = dumm.next

    # remove node form LinkedList
    # P     node    N
    def remove(self, node: DoubleNode):
        preN = node.pre
        next = node.next
        preN.next = next
        next.pre = preN

    # insert node to right
    def insert(self, node: DoubleNode):
        preNode = self.RightNode.pre
        nxtNode = self.RightNode
        preNode.next = nxtNode.pre = node
        node.pre, node.next = preNode, nxtNode

    def get(self, key: int) -> int:
        if key in self.cache:
            # DOTO:update most resent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:            
            self.remove(self.cache[key])
        self.cache[key] = DoubleNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            # remove
            remove = self.LeftNode.next
            self.remove(remove)
            del self.cache[remove.key]
