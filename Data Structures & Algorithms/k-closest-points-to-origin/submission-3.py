class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [] 
        for x, y in points:
            d = (x - 0)**2 + (y-0)**2
            heapq.heappush(dis, (-abs(d), [x,y]))

            if len(dis) > k:
                heapq.heappop(dis)
    
        return [i[1] for i in dis]