"""_summary_
Leetcode 71. Simplify Path
Using stack to store every path.
#Leetcode150
Time:O(n)
Space:O(n)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        # /home/
        for c in path + "/":  # add "/", easy to deal with last part of path
            if c == "/":
                if cur == "..":
                    if len(stack) > 0:
                        stack.pop()
                elif cur != "" and cur != ".":  # condition to append
                    stack.append(cur)
                cur = ""
            else:
                cur += c  # tmp path

        return "/" + "/".join(stack)

        """_summary_
        easy way to understand alg.
        splite string by / -> 
        1.".." -> pop if not empty
        2. "." "" -> do nothing
        3."asdasd" -> add stack
        
        """
    def simplifyPath2(self, path: str) -> str:
        stack = []
        splitString = path.split("/")
        for str in splitString:
            if str == "..":
                if stack:
                    stack.pop()
            elif str == "." or str == "":
                continue
            else:
                stack.append(str)

        res = "/" + "/".join(stack)
        return res
