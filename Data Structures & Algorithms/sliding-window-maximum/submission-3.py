class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
    
        for r, num in enumerate(nums):
            heapq.heappush(heap, (-num, r))
            # check to see if we have a valid window?
            if r >= k - 1:
                # while the large value is not in window pop it
                l = r - k + 1
                print(heap[0][1], ' l: ', l, ' r: ', r)
                while heap[0][1] <  l:
                    print('poping')
                    heapq.heappop(heap)
                print(heap, '\n')
                res.append(-heap[0][0])



        return res