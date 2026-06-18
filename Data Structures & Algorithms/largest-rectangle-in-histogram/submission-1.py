class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        heights = [7, 1, 7, 2, 2, 4]
        """

        maxA = 0
        stack = []
        for idx, h in enumerate(heights):
            i = idx
            # if previous current height is less that the previous height (top of stack)
            while stack and stack[-1][0] > h: 
                old_h, old_idx = stack.pop()
                # calculate the maxA 
                area = old_h * (idx - old_idx)
                maxA = max(maxA, area)
                i = old_idx # since we can extend to the left lets update the start
            stack.append([h, i])

        for h, i in stack: 
            area = h * (len(heights) - i)
            maxA = max(area, maxA)
        return maxA