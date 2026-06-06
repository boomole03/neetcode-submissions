"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)

        start = end = float('-inf')

        for interval in intervals:
            if interval.start < end: 
                return False

            start, end = interval.start, interval.end
        return True