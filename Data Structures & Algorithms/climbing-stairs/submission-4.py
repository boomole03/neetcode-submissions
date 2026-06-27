class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 1 or 2
        n = 3
            1 2 
            2 1
            1 1 1

        n = 4
            2 2
            2 1 1
            1 1 2
            1 2
            1 1 1
        """
        if n <= 2: 
            return n
        one = 1
        two = 2
        for i in range(3, n+1):
            one, two = two, one+ two
        return two