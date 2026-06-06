class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Input: target = 10, nums = [2,1,5,1,5,3]

        Output: 3

        # find the minimal length of a subarray where the total sum is greater than or equal to target

        [2, 1, 5, 1, 5, 3]
         l = 0 
         r = 5
         ts = 14
         res = 1 
        """

        l = 0 
        res = 0
        ts = 0
        for r in range(len(nums)):
            ts += nums[r]

            while ts >= target:
                if res == 0:
                    res = r - l + 1
                else: 
                    res = min(res, r - l + 1)
                ts -= nums[l]
                l += 1
        
        return res