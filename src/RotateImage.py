from typing import List

"""_summary_
Leetcode #48
Returns:
    _type_: _description_
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # if 4x4 matrix, l=0 r=3
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                # i will be shift position of the matrix rotation.
                top, botton = l, r
                # save top left
                topLeft = matrix[top][l + i]

                # botton left to top left
                matrix[top][l + i] = matrix[botton - i][l]

                # botton right to botton left
                matrix[botton - i][l] = matrix[botton][r - i]

                # top right to botton left
                matrix[botton][r - i] = matrix[top + i][r]

                # top left to top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1
