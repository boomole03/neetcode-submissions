class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        i = 0
        while i < len(nums): 
            current_stack = []
            for n in res:
                # push unchanged
                print('n', n)
                current_stack.append(n.copy())
                n.append(nums[i])
                current_stack.append(n.copy())
            res = current_stack
            i+=1
        return res

        