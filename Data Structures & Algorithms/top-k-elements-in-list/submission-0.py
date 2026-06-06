class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for i in freq.keys():
            f = freq[i]
            if len(heap) < k: 
                heapq.heappush(heap, (f, i))
            else: 
                if heap[0][0] < f:
                    heapq.heappushpop(heap, (f, i))

        return [i[1] for i in heap]

        