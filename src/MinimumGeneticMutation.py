"""_summary_
Leetcode 433. Minimum Genetic Mutation
Using BFS to try all combination of gene
#Leetcode150
Time:O(n)
Space:O(n)
"""

from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankset = set(bank)
        options = ["A", "T", "C", "G"]
        q = deque()
        q.append([startGene, 0])

        visited = set()
        visited.add(startGene)

        while q:
            gen, c = q.popleft()
            if gen == endGene:
                return c
            for i in range(len(gen)):  # loop from top to end
                for j in options:
                    # assemble the new gene
                    newGen = gen[:i] + j + gen[i + 1 :]
                    if newGen in bankset and newGen not in visited:
                        q.append([newGen, c + 1])
                        visited.add(newGen)
        return -1
