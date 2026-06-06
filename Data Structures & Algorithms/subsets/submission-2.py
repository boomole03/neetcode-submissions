class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 3]
        """
        res = []
        stack = []
        def dfs(idx):
            if idx == len(nums):
                res.append(stack.copy())
                return

            # move pointer forward and update stack
            stack.append(nums[idx])
            dfs(idx+1)  
            stack.pop()
            dfs(idx+1)


        dfs(0)
        return res