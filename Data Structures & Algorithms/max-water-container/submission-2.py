class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        m = 0 

        while(l < r):
            print('r ', r, ' l ', l )
            s = min(heights[l], heights[r]) * (r-l)
            m = max(s, m)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return m