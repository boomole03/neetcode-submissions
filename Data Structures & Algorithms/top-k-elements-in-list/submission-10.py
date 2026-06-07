class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        heap = []

        for idx, count in counter.items():
            heapq.heappush(heap, (count, idx))
            # if heap larger than k
            if len(heap) > k:
                # remove the smallest value
                heapq.heappop(heap)

        return [i[1] for i in heap]

"""
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        dic = Counter(nums)
        heap = []
        for key in dic.keys():
            heapq.heappush(heap, (dic[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for value, key in heap]
        
"""