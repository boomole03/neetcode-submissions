class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, i in enumerate(nums):
            print(i, index, seen)
            comp = target - i
            if comp in seen:
                # print([seen[comp], index])
                return [seen[comp], index]

            seen[i] = index
        return []