class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        stones[i] = weight of the ith store
        at each step we: 
            1) two heavists wieght x and y
            2) x == y, remove both from heap
            3) x < y, remove y and add y - x to heap
        """

        heap = [ -w for w in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1: # as long as we have at least two nodes we can break this down
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if abs(y - x):
                heapq.heappush(heap, -abs(y-x))

        return -heap[0] if len(heap) == 1 else 0