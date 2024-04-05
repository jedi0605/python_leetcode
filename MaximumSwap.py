from collections import Counter, deque
import heapq
from typing import List

"""_summary_
LeetCode 670. Maximum Swap
T: O(n * m) # A,A,A * N
S: O(1)
#Meta Tag
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        # Keep track of the last index of each digit in the number
        last_seen = {int(digit): i for i, digit in enumerate(digits)}

        # Iterate over each digit in the number
        for i, digit in enumerate(digits):
            # Check if there is a larger digit after the current digit
            for j in range(9, int(digit), -1):
                if j in last_seen and last_seen[j] > i:
                    # Swap the digits and return the result
                    digits[i], digits[last_seen[j]] = digits[last_seen[j]], digits[i]
                    # digits[i], digits[last_seen[j]] = digits[last_seen[j]], digits[i]
                    return int("".join(digits))

        # If no swap was made, return the original number
        return num

        # Brute force
        # A = list(str(num))
        # ans = A[:]
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         A[i],A[j] = A[j],A[i] # swap
        #         if A > ans:
        #             ans = A[:]
        #         A[i],A[j] = A[j],A[i] # swap back
        # return int("".join(ans))
