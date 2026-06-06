class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums: 
            if len(heap) < k:
                heapq.heappush(heap, i)
            else: 
                if i > heap[0]:
                    heapq.heappushpop(heap, i)
        k_lar = heap[0]
        return k_lar
        