from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # two path
        arr = [1] * len(ratings)
        # left to right
        for i in range(1, len(arr)):
            if ratings[i] > ratings[i - 1]:
                arr[i] = arr[i - 1] + 1
        # left to right
        for i in range(len(arr) - 1 - 1, -1, -1):
            if ratings[i] > ratings[i + 1] and arr[i]<=arr[i+1]:
                arr[i] = arr[i + 1] + 1
        return sum(arr)
        # n = len(ratings)
        # candys = [1] * n

        # for i in range(1, n):
        #     if ratings[i - 1] < ratings[i]:
        #         candys[i] = candys[i - 1] + 1

        # for i in range(n - 2, -1, -1):
        #     if ratings[i] > ratings[i + 1] and candys[i] <= candys[i + 1]:
        #         candys[i] = candys[i + 1] + 1

        # return sum(candys)
