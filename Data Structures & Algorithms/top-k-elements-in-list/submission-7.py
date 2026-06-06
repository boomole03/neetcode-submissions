class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        - using a heap to keep track of the count
        """

        dic = Counter(nums)
        heap = []
        for key in dic.keys():
            heapq.heappush(heap, (dic[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for value, key in heap]
        