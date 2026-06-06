class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_stack = []
        for i in tokens:
            if i == '+':
                math_stack.append(math_stack.pop() + math_stack.pop())
            elif i == '-':
                a, b = math_stack.pop(), math_stack.pop() 
                math_stack.append(b - a)
            elif i == "*":
                math_stack.append(math_stack.pop() * math_stack.pop())
            elif i == "/":
                a, b = math_stack.pop(), math_stack.pop()
                math_stack.append(int(float(b) / a))
            else:
                math_stack.append(int(i))
        return math_stack[0]
        