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
        Input: intervals = [(0,40),(5,10),(15,20)]

        Output: 2
        0 ----------------------------------- 40
               5 ----- 10 
                               15 ------ 20
        """

        count = 0

        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        e = 0
        for s in range(0, len(start)):
            print(start[s], end[e])
            if start[s] < end[e]:
                count +=1
            else:
                e+=1
        return count        
        
        