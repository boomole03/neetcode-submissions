class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Input: nums = [3,4,5,6,1,2]

        1 2 3 4 5 6
        6 1 2 3 4 5 
        5 6 1 2 3 4
        4 5 6 1 2 3
        Output: 1


        [3,4,5,6,1,2]
        l    m     r
             l m   r
               l m r
        # check to if which size is smaller

        """

        l, r = 0, len(nums) - 1
        while l < r: 
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m

        return nums[l]