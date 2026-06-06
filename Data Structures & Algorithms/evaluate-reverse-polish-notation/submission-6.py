class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for char in tokens: 
            if char in '+-/*':
                if char == '+':
                    a = stack.pop()
                    b = stack.pop()
                    res = a + b
                elif char == '-':
                    a = stack.pop()
                    b = stack.pop()
                    res = b - a
                elif char == '*':
                    a = stack.pop()
                    b = stack.pop()
                    res = a * b
                else: 
                    a = stack.pop()
                    b = stack.pop()
                    res = int(b / a)
                stack.append(res)
                
            else: 
                stack.append(int(char))

        return stack[-1]