from typing import List

"""_summary_
for c in ransomNote:
    if ransomNote.count(c) > magazine.count(c)
        retrun false
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = set(ransomNote)
        for i in a:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True