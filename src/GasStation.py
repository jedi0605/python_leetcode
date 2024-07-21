from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        totalCost = 0
        res = 0
        for i in range(len(gas)):
            totalCost = totalCost + gas[i] - cost[i]
            if totalCost < 0:
                totalCost = 0
                res = i + 1
        return res
