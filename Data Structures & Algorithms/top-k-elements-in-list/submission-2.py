class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [ [] for _ in range(len(nums) + 1)] # the bucket we use to for bubble sort

        for i in nums: 
            count[i] += 1 

        for key, value in count.items(): 
            freq[value].append(key)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: 
                    return res