class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(k):
            if k == 0 :
                # if k is 2 or less then we know the
                # base case
                return 1
            if k < 0:
                return 0
            if k not in memo:
                memo[k] = dp(k-1) + dp(k-2)
            return memo[k]

        return dp(n)