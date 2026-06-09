class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = float('inf')
        for price in prices:
            if price > prev:
                # we might have a new time to buy
                res = max(res, price - prev)

            else:
                prev = price

        return res