class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 

        def can_eat(k):
            t = 0
            for p in piles: 
                t += math.ceil(p / k)
                if t > h: 
                    return False

            return True

        while l < r:
            m = (r + l) // 2

            if can_eat(m):
                r = m 
            else: 
                l = m + 1

        return l