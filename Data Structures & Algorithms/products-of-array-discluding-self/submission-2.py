class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,4,6]
        i = 0
        pre = 1
        new pre = (1 * nums[i])
    
        nums = [1, ]
    
        # post = 1
        # new post = 1
        # nums = [1, 2, 8, 48]

        # Output: [48,24,12,8]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for n in range(len(nums) -1, -1, -1):
            res[n] *= postfix
            postfix *= nums[n]
            
        return res