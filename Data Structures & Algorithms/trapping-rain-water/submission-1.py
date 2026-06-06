class Solution:
    def trap(self, height: List[int]) -> int:
        """ 
        possible we don't trap any water so let's return -1 or something

        use two pointer

        """

        if not height:
            return 0

        max_trap = 0
        l, r = 0, len(height) - 1
        l_max = r_max = 0

        while l < r: 
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if l_max > r_max:
                max_trap += r_max - height[r]
                r -=1
            else: 
                max_trap += l_max - height[l]
                l +=1


        return max_trap