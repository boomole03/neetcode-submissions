class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        nums.sort()
        print('Nums: ', nums, 'lenght', len(nums))

        curr_max = 1
        final_max = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] + 1 == nums[i+1]:
                curr_max += 1
            else: 
                final_max = max(curr_max, final_max)
                curr_max = 1
            print(i)
        final_max = max(curr_max, final_max)
        return final_max



        