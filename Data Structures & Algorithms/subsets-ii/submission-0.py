class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 1] -> [1, 1, 2]
        [] -> [] -> [2]
           -> [1] -> [1, 1]
                  -> [1, 1] -> [1, 1, 2]  
                  
                  -> [1, 2]
        """
        res = []
        nums.sort()

        def backtrack(idx, curr):
            if idx == len(nums):
                res.append(curr.copy())
                return

            # include
            curr.append(nums[idx])
            backtrack(idx + 1, curr)

            curr.pop()
            n_idx = idx + 1
            while n_idx < len(nums) and nums[n_idx] == nums[idx]:
                n_idx +=1 
            backtrack(n_idx, curr)

        backtrack(0,[])
        return res