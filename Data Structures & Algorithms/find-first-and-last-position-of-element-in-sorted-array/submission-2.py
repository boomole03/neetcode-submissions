class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        [5, 7, 7, 8, 8, 10] target = 8 -> [3, 4]
         l     m         r
        # 7 ! >= 8 : l = m + 1
                  l  m  r
                  return 4 

        [5, 7, 7, 8, 8, 10] target = 9 
         l     m         r
        # 7 ! >= 9 : l = m + 1
                  l  m  r
                       l,r
        """
        n = len(nums)
        def binarySearch(target):
            l, r = 0, n
            while l < r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        start = binarySearch(target)
        if start == n or nums[start] != target:
            return [-1, -1]

        return [start, binarySearch(target + 1) - 1]