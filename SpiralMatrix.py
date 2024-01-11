from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, botton = 0, len(matrix)
        res = []
        while top < botton and left < right:
            # left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # top to down
            for i in range(top, botton):
                res.append(matrix[i][right - 1])
            right -= 1

            # [1,2,3]
            if not (left < right and top < botton):
                break
            # right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[botton - 1][i])
            botton -= 1

            # botton to top
            for i in range(botton - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res