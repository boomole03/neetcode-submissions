class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        curr_array = 0
        for i in nums:

            if curr_array < 0:
                curr_array = 0
            curr_array += i
            m = max(m, curr_array)

        return m
        