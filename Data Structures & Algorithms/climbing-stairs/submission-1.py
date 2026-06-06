class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n is the amount of steps we have to climp

        we can only climb 1 or 2 steps at a time...

        n = 1: we can only climp once
        n = 2: we can 1 + 1 or 2 , so two different ways  
        n = 3: if we take 1 step... 2 steps left, how many steps for 2 (2)
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        """
        if n <= 2:
            return n

        one = 1
        two = 2
        for i in range(3, n+1):
            one, two = two, one + two 
            # dp[i] = dp[i - 2] + dp[i-1]

        return two