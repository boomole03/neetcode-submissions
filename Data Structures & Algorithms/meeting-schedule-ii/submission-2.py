"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        0 ------------------------------------------------- 40
                5 ----- 10
                              15 ------ 20
        """
        count = 0
        end = sorted(i.end for i in intervals)
        start = sorted(i.start for i in intervals)
        e = 0
        for s in range(len(start)):
            if start[s] < end[e]:
                count +=1 
            else:
                e +=1

        return count