class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLowerBound():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l
        
        def findUpperBound():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
        if not nums:
            return [-1, -1]
        
        low = findLowerBound()
        high = findUpperBound()
        
        # validate target exists
        if low <= high:
            return [low, high]
        return [-1, -1]
