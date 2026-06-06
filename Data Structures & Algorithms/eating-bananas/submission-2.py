class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """ 
        Input: piles = [1,4,3,2], h = 9

        what is the rate you can finish all bananas in the given h time frame


        Output: 2

        [1, 2, 3, 4] => array of the of min banana i can eat and max i can eat

        """

        def canEat(k):
            count = 0
            for n in piles:
                count += math.ceil(n / k)
                if count > h: 
                    return False
            return True

        l, r = 1, max(piles)

        while l < r: 
            m = l + (r - l) // 2

            # check to see if valid
            if canEat(m):
                r = m 
            else: 
                l = m + 1
        return l