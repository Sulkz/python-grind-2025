"""
Only need focus on the difference of the number of intervals not present in the new list and the original 
so just find that difference we dont care about the actualy pairs which are removed
"""

class Solution(object):
    def eraseOverlapIntervals(intervals):
        intervals.sort(key=lambda x:x[1])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] <= interval[0]:
                merged.append(interval)
        return len(interval) - len(merged)


Solution.eraseOverlapIntervals([[1,3],[2,6],[8,10],[15,18]])