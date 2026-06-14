class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        mono_stack = [
        (38, 0)
        (30, 0)]
        """
        res = [0] * len(temperatures)
        mono_stack = []

        for idx, temp in enumerate(temperatures):
            while mono_stack and mono_stack[-1][0] < temp: 
                # we have found a hotter temp
                top = mono_stack.pop()
                res[top[1]] = idx - top[1]

            mono_stack.append((temp, idx))
                

        return res