class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = defaultdict(int)
        for n in nums:
            num_counter[n] += 1

        idx_counter = [[] for i in range(len(nums) + 1)]
        for val in num_counter:
            idx_counter[num_counter[val]].append(val)

        res = []

        for i in range(len(idx_counter) - 1, 0 , -1):
            for num in idx_counter[i]:
                res.append(num)
                if len(res) == k:
                    return res

        