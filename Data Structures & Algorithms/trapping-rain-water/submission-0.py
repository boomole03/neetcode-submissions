class Solution:
    def trap(self, height: List[int]) -> int:
        # no way to trap water
        if not height: 
            return 0
        water = 0
        l, r = 0, len(height) - 1
        l_max = r_max = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if l_max > r_max:
                water += r_max - height[r]
                r -=1
            else: 
                water += l_max - height[l]
                l +=1
        return water
            
            
        