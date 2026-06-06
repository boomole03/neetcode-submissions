class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens: 
            if i in '+-*/':
                # do the math
                if i == '+':
                    val_1 = stack.pop()
                    val_2 = stack.pop() 
                    m = val_1 + val_2
                    stack.append(m)
                elif i == '-':
                    val_1 = stack.pop()
                    val_2 = stack.pop() 
                    m = val_2 - val_1
                    stack.append(m)
                elif i == '*':
                    val_1 = stack.pop()
                    val_2 = stack.pop() 
                    m = val_1 * val_2
                    stack.append(m)
                else: 
                    val_1 = stack.pop()
                    val_2 = stack.pop() 
                    m = int(val_2 / val_1)
                    stack.append(m)
            else: 
                stack.append(int(i))
            
        return stack[-1]
        