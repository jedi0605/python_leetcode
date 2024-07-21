from typing import List

"""_summary_
Leetcode #73 Set Matrix to zero
Ref:https://www.youtube.com/watch?v=T41rL0L3Pnw&ab_channel=NeetCode
======= Ver1.======
Using two array to track which [m][n] will trun to zero.
rows[]
cols[]
======= Ver2.======
Ver1 will using O(m+n) extra memory space.
To optimize memory. using [m][n] matrix.
[0][col] -> to mapping rows[] func
[row][0] -> to mappsing cols[] func.
rowZero : PLUS one more space to track rows[] cols[] overlap

Returns:
    _type_: _description_
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        colsTrack = [1] * COLS
        rowsTrack = [1] * ROWS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    colsTrack[c] = 0
                    rowsTrack[r] = 0

        for r in range(ROWS):
            for c in range(COLS):
                if colsTrack[c] == 0 or rowsTrack[r] == 0:
                    matrix[r][c] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowToZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        rowToZero = True
                    else:
                        matrix[r][0] = 0

        # Fill out m-1,n-1
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # Dill with row0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowToZero:
            for c in range(COLS):
                matrix[0][c] = 0
