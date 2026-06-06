class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1,3],[1,5],[6,7]] -> [[1,5],[6,7]]

        res = []
        
        """

        res = []
        intervals.sort()
        for start, end in intervals:
            if res and start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])

        return res