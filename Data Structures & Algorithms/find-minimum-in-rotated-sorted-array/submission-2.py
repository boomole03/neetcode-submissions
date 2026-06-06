class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: 
            return None

        l, r = 0, len(nums) -1
        while l < r: 
            m =  l + (r - l) // 2
            print('left: ', l, ' mid: ', m, ' right: ', r)
            if nums[m] < nums[r]: 
                r = m
            else:
                l = m + 1
        return nums[l]