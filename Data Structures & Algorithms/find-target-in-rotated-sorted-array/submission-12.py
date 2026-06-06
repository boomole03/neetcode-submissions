class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        Input: nums = [3,4,5,6,1,2], target = 1
        check if m == target
        else what side do we check
        if left if less than m 
            [3, 4, 5]
        else: 
            [6, 1, 2]
        Output: 4

        """
        
        l, r = 0, len(nums) -1 

        while l <= r: 
            m = l + (r - l) // 2

            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]: 
                    l = m + 1
                else:
                    r = m - 1
            else: 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: 
                    l = m + 1


        return -1
















