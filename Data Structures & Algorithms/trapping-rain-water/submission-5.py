class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) -1
        left_bound = right_bound = 0

        while l < r:
            left_bound = max(left_bound, height[l])
            right_bound = max(right_bound, height[r])

            if left_bound < right_bound:
                res += left_bound - height[l]
                l +=1
            else:
                res += right_bound - height[r]
                r -=1

        return res