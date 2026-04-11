"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #need to sort the list by start times
        #(a, b) (c,d)
        # conflict if c < b

        intervals = sorted(intervals, key=lambda x: x.start)
        
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True
            

