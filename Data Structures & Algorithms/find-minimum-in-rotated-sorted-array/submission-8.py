class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        key here is to find the part of the array that is sorted and check if value is in there else it's in the other
        side
        """

        l, r = 0, len(nums) - 1
        while l < r:
            m = ((r - l) // 2 + l)
            if nums[m] < nums[r]:
                r = m
            else: 
                l = m + 1     
        return nums[l]