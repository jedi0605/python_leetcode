from collections import Counter


class Solution:
    def minWindow2(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have (let lease compare for tracking )
        have, need = 0, len(countT)
        resLen = float("infinity")
        res = [-1, -1]
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            ## when count fully match have+=1.
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # compare mini result
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                # decrease the length of the result, also we use while above
                # if after decreasing the length of result from left side and have is same
                # as need then we can update the result as we have to return min length
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen == float("infinity"):
            return ""
        else:
            return s[l : r + 1]  # python have plus1 to inclusive the end of char

    def minWindow(self, s: str, t: str) -> str:
        s_count, t_count = Counter(), Counter(t)
        # Define variables
        s_count, t_count = Counter(), Counter(t)

        l, r = 0, 0

        results = []

        while r <= len(s) - 1:
            # Find valid window
            s_count[s[r]] += 1
            r += 1
            if s_count & t_count != t_count:
                continue

            # Minimize this window
            while l < r:
                s_count[s[l]] -= 1
                l += 1
                if s_count & t_count == t_count:
                    continue
                results.append(s[l - 1 : r])
                break

        # Return result
        if not results:
            return ""
        return min(results, key=len)
