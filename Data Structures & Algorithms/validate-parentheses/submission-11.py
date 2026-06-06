class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {"}": "{", ")": "(", "]": "["}
        stack = []

        for char in s: 
            if char in '])}':
                if not stack or stack[-1] != par_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False
