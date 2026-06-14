class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        we can use a heap to keep track of the largest value in a given window
        """

        heap = []
        res = []
        for r in range(len(nums)):
            # build the heap with the val (-val, for a max heap) and index
            heapq.heappush(heap, (-nums[r], r))
            
            # if the heap size hits a certian limit then it's a valid window
            if r >= k - 1: 
                l = r - k + 1
                while heap[0][1] < l: 
                    heapq.heappop(heap) # invalid

                res.append(-heap[0][0])
                # find the largest in the given window

        return res
        