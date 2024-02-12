from typing import List

"""_summary_
Using two maps to track word exist or not
Using HashMap to track each strings are anagram or not.
case : strs = ["eat","tea","tan","ate","nat","bat"]
eat -> [1e 1a 1t]
tea -> [1e 1a 1t]
Using array[26] be the hashmap key
O(m * n) # m len of strs, n char of each string
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key in res:                
                res[key].append(s)
            else:
                res[key] = [s]
        print(res.values())
        return res.values()