class Solution:
    def trap(self, height: List[int]) -> int:
        """
        0, 2, 0, 3, 1, 0, 1, 3, 2, 1
                 l                    
                    r
        l_max = 3
        r_max = 3
        
        condition:
            if left small:
                
            else: 
                3 - 1

        res = 2 + 2 + 3 + 2
        """

        l, r = 0, len(height) - 1
        l_max = r_max = 0
        res = 0
        while l < r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)

            # if left is smaller we need to move l pointer
            if l_max < r_max: 
                res += l_max - height[l]
                l += 1
            else:
                res += r_max - height[r]
                r -= 1

        return res