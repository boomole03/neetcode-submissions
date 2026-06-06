class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        m = 0

        for i in numSet:
            if (i - 1) not in numSet: 
                l = 1
                while (i + l) in numSet:
                    l += 1
                m = max(m, l)

        return m
        