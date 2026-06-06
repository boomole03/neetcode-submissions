class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]  # Start with the empty subset
        for num in nums:
            # For each number, add it to all existing subsets
            res += [curr + [num] for curr in res]
            print(res)
        return res

        