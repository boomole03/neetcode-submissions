class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            nums = [1, 2, 4, 6]
            i = 0 pre = 1 res = [1, 0, 0, 0]
            i = 1 pre = 2 res = [1, 1, 0, 0]
            i = 2 pre = 8 res = [1, 1, 2, 0]
            i = 3 pre = 8 res = [1, 1, 2, 8]

            # now do reverse
        """

        pre = 1
        res = [0] * len(nums)
        for i in range(0, len(nums)):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
