class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [] 
        for x, y in points:
            d = x*x + y*y
            heapq.heappush(dis, (-(d), [x,y]))

            if len(dis) > k:
                heapq.heappop(dis)
    
        return [i[1] for i in dis]