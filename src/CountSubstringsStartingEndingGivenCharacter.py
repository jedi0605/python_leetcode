"""_summary
3084. Count Substrings Starting and Ending with Given Character
"""

import collections


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = collections.Counter()
        res = 0
        for ch in s:
            cnt[ch] += 1
            if ch == c:
                res += cnt[c]
        return res
    
        # tmp = set()

        # def dfs(start, end):
        #     if start > end or end > len(s) or start > len(s):
        #         return

        #     tmp.add((start, end))
        #     print((start,end))
        #     if end != len(s):
        #         dfs(start, end + 1)
        #     if((start+1, end) not in tmp):
        #         dfs(start + 1, end)

        # dfs(0, 0)
        # res = 0
        # print(tmp)
        # for tmp_idx in tmp:
        #     sub = s[tmp_idx[0] : tmp_idx[1]]
        #     if sub.startswith(c) and sub.endswith(c):
        #         res += 1
        # return res
