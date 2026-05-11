"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = [ i.start for i in intervals ]
        end = [ i.end for i in intervals ]
        start.sort()
        end.sort() 

        s = 0 
        e = 0 
        max_meetings = 0 
        count = 0 

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            max_meetings = max(max_meetings, count)

        return max_meetings