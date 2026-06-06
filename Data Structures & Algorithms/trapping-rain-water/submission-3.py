class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
    
        while l < r:
            # most we can have rn:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)

            if l_max < r_max:
                res += l_max -  height[l] 
                l += 1
            else:
                res += r_max -  height[r]
                r -= 1

        return res