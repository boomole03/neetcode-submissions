class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [30,38,30,36,35,40,28] -> [1,4,1,2,1,0,0]
            i 

        while stack and is the value large than the top? pop from stack and append to the results

        """


        res = [0] * len(temperatures)
        mono_stack = []

        for index, temp in enumerate(temperatures):
            while mono_stack and mono_stack[-1][0] < temp:
                res[mono_stack[-1][1]] = index - mono_stack[-1][1]
                mono_stack.pop()
            mono_stack.append((temp, index))

        return res