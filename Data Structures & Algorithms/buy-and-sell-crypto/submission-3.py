class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_time = 0
        buy = float('inf')
        for i in prices: 
            if i <= buy: 
                buy = i
            else: 
                best_time = max(best_time, i - buy)

        return best_time


        