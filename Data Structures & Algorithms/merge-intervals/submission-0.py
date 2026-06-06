class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Input: intervals = [[1,3],[1,5],[6,7]] -> .....

        if intervals are in values [x, y]... sort based on x 

        y is larger then next x

        Output: [[1,5],[6,7]]


        """
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort() 

        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] >= x:
                res[-1] = [res[-1][0], max(res[-1][1], y)]
            else:
                res.append([x, y])

        return res