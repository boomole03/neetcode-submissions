class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t in '+-/*':
                if t == '+':
                    a = stack.pop()
                    b = stack.pop()
                    res = a + b
                elif t == '-':
                    a = stack.pop()
                    b = stack.pop()
                    res = b - a
                elif t == '*':
                    a = stack.pop()
                    b = stack.pop()
                    res = a * b
                else: 
                    a = stack.pop()
                    b = stack.pop()
                    res = int(b / a)
            
                stack.append((res))
            else:
                stack.append(int(t))


        return stack[-1]