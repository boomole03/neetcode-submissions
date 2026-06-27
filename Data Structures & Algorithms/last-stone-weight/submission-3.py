class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap to keep track of the two largest rocks
        heap = []

        # create the max-heap
        for s in stones:
            heapq.heappush(heap, -s)

        # now we need to pop the two largest value and destroy the stones
        while len(heap) > 1: # while we have at least two stones
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)

            if s1 == s2: 
                continue
            else: 
                res = abs(s1 - s2)
                heapq.heappush(heap, -res)

        return -heap[0] if heap else 0