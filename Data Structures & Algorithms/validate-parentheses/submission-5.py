class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {"{" : "}", "(" : ")", "[" : "]"}
        stack = []

        for i in s: 
            if i in '])}':
                if stack and par_map[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True
        