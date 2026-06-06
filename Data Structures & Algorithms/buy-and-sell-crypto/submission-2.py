class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        p = prices[0] # 10
        for i in prices:
            if i < p: # i 8 p 10, i 5 p 8, i 6 p 5, i 7 p6, 
                p = i # p 8, p 5
            print('i: ', i, 'p ')
            res = max(res, i - p) # -1, 
        return res