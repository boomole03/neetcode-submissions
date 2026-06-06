class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1,7,2,5,4,7,3,6]
        l 
                       r

        max_water
        water = min(l, r) * (r - l + 1)
        """
        

        max_water = float('-inf')

        l, r = 0, len(heights) -1

        while l < r: 
            water = min(heights[l], heights[r]) * (r - l)
            print('l : ', l, ' r: ', r, ' water: ', water)
            if heights[l] < heights[r]:
                l +=1 
            else: 
                r -=1


            max_water = max(max_water, water)

        return max_water