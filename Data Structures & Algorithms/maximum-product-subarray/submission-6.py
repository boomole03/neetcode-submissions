class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [1,2,-3,4] -> [4] -> 4

        neg = 1, 2, -6, -24
        pos = 1, 2, -3, 4
        temp = 

        """

        res = nums[0]
        currMin, currMax = 1, 1
        for num in nums: 
            temp = currMax
            # new max can either be num * currMax (positive * postive), num * currMin (negative value turned postive) 
            currMax = max(num * currMax, num * currMin, num) 

            # new min can either be [num * temp] (if num is negative and currMax is positive) or [num * currMin] (if num i  negative and currMin is postivie (or maybe flipped))
            currMin = min(num * temp, num * currMin, num)
            res = max(res, currMax)
            print(currMin, currMax)

        return max(res, currMax)