class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        mon_stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)): 
            while mon_stack and (temperatures[i] > mon_stack[-1][1]):
                top = mon_stack.pop()
                result[top[0]] = i - top[0]
            mon_stack.append((i, temperatures[i]))
        return result   