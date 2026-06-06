class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = [(0, temperatures[0])]

        """

        38, 1
        30, 0 
        """

        for i in range(1, len(temperatures)):
            while mono_stack and temperatures[i] > mono_stack[-1][1]:
                print(mono_stack)
                top = mono_stack.pop() 
                res[top[0]] = i - top[0]

            mono_stack.append((i, temperatures[i]))
        return res