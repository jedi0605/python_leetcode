from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        # tmp = [ x for x in arr if x!=' ']
        # for i in arr:
        #     if i!="":
        #         tmp.append(i)
                
        i =0
        j = len(arr) -1
        while i<j:
            (arr[i], arr[j]) = (arr[j],arr[i])
            i+=1
            j-=1
        return ' '.join(arr)
    
