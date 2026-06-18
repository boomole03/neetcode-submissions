class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles[i] is the # of bananas in the ith pile
        h is the # of hours you have to eat all the bananas

        find the min k so to eat all bananas in the given h
        """
        def can_eat(k): 
            hour = 0
            for i in piles:
                t = math.ceil(i / k)
                print(t)
                hour += t
                if hour > h: 
                    return False

            return True
            
        l, r = 1, max(piles)
        while l < r:
            m = ((r - l) // 2 + l)
            res = can_eat(m)
            print('m: ', m, ' res: ', res)
            # we need to check if this is valid
            if can_eat(m):
                r = m
            else: 
                l = m + 1
        return l 
