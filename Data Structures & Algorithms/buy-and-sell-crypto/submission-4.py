class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for p in prices:
            if p > buy:
                res = max(p - buy, res)
            else: 
                buy = p

        return res