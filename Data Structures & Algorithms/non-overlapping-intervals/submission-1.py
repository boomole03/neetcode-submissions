class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        res = 0
        prevEnd = intervals[0][1]
        for x, y in intervals[1:]:
            if x >= prevEnd:
                prevEnd = y
            else:
                res += 1
                prevEnd = min(y, prevEnd)

        return res