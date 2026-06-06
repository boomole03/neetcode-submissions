class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        - two pointer approach, we only need need to keep track of where the 0 is and where the 2 is
        """
        
        l, r = 0, len(nums) - 1
        i = 0

        def swap(x, y):
            t = nums[x]
            nums[x] = nums[y]
            nums[y] = t
    
        while i <= r:
            # what is l:
            if nums[i] == 0:
                # swap the left and i
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                # swap the right and i
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
            