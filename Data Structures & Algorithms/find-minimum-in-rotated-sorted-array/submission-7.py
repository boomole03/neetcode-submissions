class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        """
        trick with this is one part of the half will be in order

        [3, 4, 5, 6, 1, 2]
         l
               m
                        r
        in order
        """
        while l < r:
            m = (r + l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]