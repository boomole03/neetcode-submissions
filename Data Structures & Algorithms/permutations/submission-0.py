class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
                                [1, 2, 3]
                [1]:[T,F,F]     [2]:[F,T,F]     [3]:[F,F,T]
             
        """

        res = []

        def dfs(perm, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            # build next perm
            for n in range(len(nums)):
                if not used[n]:
                    used[n] = True
                    perm.append(nums[n])
                    dfs(perm, used)

                    perm.pop()
                    used[n] = False
            return



        dfs([], [False] * len(nums))
        return res