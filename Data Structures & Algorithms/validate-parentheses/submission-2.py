class Solution:
    def isValid(self, s: str) -> bool:

        par_map = {'}': '{', ']': '[', ')': '(' }
        stack = []
        for i in s: 
            if i in par_map:
                if not stack or stack[-1] != par_map[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        if stack: 
            return False
        return True