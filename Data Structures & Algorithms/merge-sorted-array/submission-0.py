class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        r1, r2 = m - 1, n - 1
        i = len(nums1) - 1

        while r2 > -1:
            # if r1 and r2 > -1
            if r1 > -1 and nums1[r1] > nums2[r2]:
                nums1[i] = nums1[r1]
                r1 -=1 
            else: 
                nums1[i] = nums2[r2]
                r2 -=1 

            i -= 1
