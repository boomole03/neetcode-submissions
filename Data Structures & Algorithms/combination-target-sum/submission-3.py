class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        def dfs(idx, total):
            if total == target: 
                res.append(stack.copy())
                return

            if total > target or idx == len(nums):
                return 
                
            stack.append(nums[idx])
            dfs(idx, total + nums[idx])

            stack.pop()
            dfs(idx+1, total)
            

        dfs(0, 0)
        return res
