class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        one part is sorted the other part isn't
        """
        l, r = 0, len(nums) - 1
        while l <= r: # check all values
            m = ((r - l) // 2 + l)
            if nums[m] == target: 
                return m
            elif nums[l] <= nums[m]:
                # left is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
            else: 
                # right is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else: 
                    r = m - 1
        return -1