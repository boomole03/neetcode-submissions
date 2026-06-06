class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for index, i in enumerate(nums): 
            t = target - i
            if t in d: 
                return [d[t], index]
            d[i] = index
        return None