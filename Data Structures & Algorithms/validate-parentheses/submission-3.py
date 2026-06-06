class Solution:
    def isValid(self, s: str) -> bool:
        if not s: 
            return True


        mapping = {'}': '{', ']':'[', ')':'('}
        stack = []

        for i in s: 
            if i in mapping: 
                if not stack or stack[-1] != mapping[i]:
                    return False
                stack.pop()
            else: 
                stack.append(i)

        return False if stack else True