class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [0,0]

        l, r = 0, len(numbers)-1
        while l < r: 
            total = numbers[l] + numbers[r]
            if total > target: 
                r -= 1
            elif total < target: 
                l += 1
            else: 
                return [l+1, r+1]

        return [0,0]