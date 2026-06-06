class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        we do two sum on a subset of the array
        things need to be sorted
        """
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: 
                # we made it to the positive values, we can't make this equal to zero so skip
                break

            if i > 0 and a == nums[i - 1]:
                # found the same number
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r: # left and rigth need to be different
                s = a + nums[l] + nums[r]
                if s > 0: 
                    r -= 1
                elif s < 0: 
                    l += 1
                else: # we found a zero sum: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1


        return res

