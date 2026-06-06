class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 3]

        [], 
        """
        # res = []
        # stack = []
        # def dfs(idx):
        #     if idx == len(nums):
        #         res.append(stack.copy())
        #         return

        #     # move pointer forward and update stack
        #     stack.append(nums[idx])
        #     dfs(idx+1)  
        #     stack.pop()
        #     dfs(idx+1)

        #     return 


        # dfs(0)

        res = [[]]
        for n in nums: 
            res += [curr + [n] for curr in res]

        return res