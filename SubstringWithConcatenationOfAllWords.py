from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) is 0:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        res = []
        word_dict = {}

        ## init word_dict. word_dict.get
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1  ## get default 0 or value+1

        ## iterate s
        ## not need check to the end. just need to check to in total_len
        for i in range(len(s) - total_len + 1):
            window = {}  ## ??
            j = 0
            while j < total_len:
                word = s[i + j : i + j + word_len]  ## get sublen of string
                if word in word_dict:
                    window[word] = window.get(word, 0) + 1
                    if window[word] > word_dict[word]:
                        break
                else:
                    break
                j += word_len
            if j == total_len:
                res.append(i)

        return res
