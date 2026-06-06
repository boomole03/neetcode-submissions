class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for n in nums: 
            if curr < 0: 
                curr = 0
            curr += n
            res = max(res, curr)

        return res