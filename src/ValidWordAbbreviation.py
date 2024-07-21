"""_summary_
LeetCode 408 Valid Word Abbreviation
T: O(n) ## worst case is word == abbr
S: O(1)
#Meta Tag
"""

from typing import List


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = 0
        abbr_ptr = 0

        while abbr_ptr < len(abbr) and word_ptr < len(word):
            if abbr[abbr_ptr].isnumeric():
                if abbr[abbr_ptr] == "0":
                    return False
                steps = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isnumeric():
                    steps = steps * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                print(steps)
                word_ptr += steps
            else:
                if abbr[abbr_ptr] != word[word_ptr]:
                    return False
                abbr_ptr += 1
                word_ptr += 1

        return abbr_ptr == len(abbr) and word_ptr == len(word)
        # abbr_ptr = 0
        # word_ptr = 0
        # while abbr_ptr < len(abbr) and word_ptr < len(word):
        #     if abbr[abbr_ptr].isdigit():

        #         if abbr[abbr_ptr] == "0":
        #             return False
        #         step = 0
        #         while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
        #             step = 10 * step + int(abbr[abbr_ptr])
        #             abbr_ptr += 1
        #         word_ptr += step
        #     else:
        #         if abbr[abbr_ptr] != word[word_ptr]:
        #             return False
        #         abbr_ptr += 1
        #         word_ptr += 1

        # return abbr_ptr == len(abbr) and word_ptr == len(word)
