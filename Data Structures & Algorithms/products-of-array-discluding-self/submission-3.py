class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 2, 4, 6] -> [48, 24, 12, 8]

        [1, 2, 8, 48]

        """

        n = len(nums)
        res = [0] * n

        prefix = 1

        for i in range(0, n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1 , -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        