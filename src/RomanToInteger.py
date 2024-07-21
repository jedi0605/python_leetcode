from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and dic[s[i]] < dic[s[i + 1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]

        return res
        # while idx < l:
        #     ## Get two
        #     tmp = s[idx : idx + 2]
        #     if tmp == "IV":
        #         res += 4
        #         idx += 2
        #     elif tmp == "IX":
        #         res += 9
        #         idx += 2
        #     elif tmp == "XL":
        #         res += 40
        #         idx += 2
        #     elif tmp == "XC":
        #         res += 90
        #         idx += 2
        #     elif tmp == "CD":
        #         res += 400
        #         idx += 2
        #     elif tmp == "CM":
        #         res += 900
        #         idx += 2
        #     else:
        #         res += dic[s[idx]]
        #         idx += 1
