class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums.sort() 

        for x in range(len(nums)):
            if nums[x] > 0: # we are in a positive number can make a sum to 0
                break

            # unique check
            if x > 0 and nums[x - 1] == nums[x]:
                continue


            y, z = x + 1, len(nums) - 1
            while y < z:
                s = nums[x] + nums[y] + nums[z]

                if s > 0:
                    z -= 1
                elif s < 0: 
                    y += 1
                else: 
                    res.append([nums[x], nums[y], nums[z]])
                    y += 1
                    z -= 1

                    while y < z and nums[y - 1] == nums[y]:
                        y += 1

        return res