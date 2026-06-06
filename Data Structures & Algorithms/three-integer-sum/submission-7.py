class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, x in enumerate(nums):
            if x > 0: # can't make zero with positive numbers
                break

            if i > 0 and nums[i -1] == x:
                continue 

            l, r = i + 1, len(nums) - 1
            while l < r:
                y = nums[l]
                z = nums[r]
                s = x + y + z

                if s == 0:
                    res.append([x, y, z])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1

        return res