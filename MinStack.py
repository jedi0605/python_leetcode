"""_summary_
Leetcode 155. Min Stack
Using two stack to track.
1. stack -> normal stack
2. minStack -> each push time will compare smellest val and append to minStack at SAME time.
    that will be much easy to operate pop func
#Leetcode150
Time:O(1)
Space:O(1)
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min) == 0:
            self.min.append(val)
        else:
            minVal = min(val, self.minStack[-1])
            self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
