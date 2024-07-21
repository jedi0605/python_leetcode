from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr = []
        length = 0
        for word in words:
            if length + len(curr) + len(word) > maxWidth:
                ## deal with justify
                s = maxWidth - length
                space = s // max(1, len(curr) - 1)
                redeamed = s % max(1, len(curr) - 1)
                for c in range(max(1, len(curr) - 1)):
                    curr[c] += " " * space
                    if redeamed > 0:
                        curr[c] += " "
                        redeamed -= 1
                res.append("".join(curr))
                curr.clear()
                length = 0

            length += len(word)
            curr.append(word)

        ## deal with last line
        last = " ".join(curr)
        lastSpace = maxWidth - len(last)
        last += " " * lastSpace
        res.append(last)
        return res
