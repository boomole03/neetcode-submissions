class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxA = 0
        stack = []

        for idx, h in enumerate(heights):
            i = idx
            while stack and stack[-1][1] > h: 
                old_idx, old_h = stack.pop() 
                maxA = max(maxA, old_h * (idx - old_idx))
                i = old_idx
            stack.append([i, h])


        for old_idx, old_h in stack: 
            maxA = max(maxA, old_h * (len(heights) - old_idx))
        return maxA