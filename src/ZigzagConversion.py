from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        increment = (numRows - 1) * 2
        
        for r in range(numRows):
            for i in range(r, len(s), increment):
                res += s[i]
                if r != 0 and r != numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res
