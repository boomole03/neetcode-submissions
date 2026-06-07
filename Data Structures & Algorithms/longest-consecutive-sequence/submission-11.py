class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for i in nums:
            curr = 1
            while i + 1 in num_set: 
                i +=1 
                curr += 1

            res = max(curr, res)

        return res
        