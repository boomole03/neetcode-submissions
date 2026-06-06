import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [] 
        res = []
        for x, y in points:
            d = math.sqrt((x - 0)**2 + (y-0)**2)
            heapq.heappush(dis, (abs(d), [x,y]))
    
        while k:
            res.append(heapq.heappop(dis)[1])
            k -= 1
        return res