from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()
        for i, ci in enumerate(citations):
            if N - i <= ci:
                return N - i
        return 0

    def hIndex2(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort(reverse=True)
        counter = 0
        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                counter += 1
        return counter


# if __name__ == "__main__":
#     s = Solution()
#     nums = [3,0,6,1,5]
#     s.hIndex(nums)
