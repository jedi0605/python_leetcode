from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.numToSquares(n)
            if n == 1:
                return True
        return False

    def numToSquares(self, n: int) -> int:
        output = 0
        while n > 0:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output
