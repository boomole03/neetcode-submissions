class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for r, num in enumerate(nums):
            heapq.heappush(heap, (-num, r))

            if r >= k - 1:
                l = r - k + 1
                while heap[0][1] < l:
                    heapq.heappop(heap)

                res.append(-heap[0][0])


        return res