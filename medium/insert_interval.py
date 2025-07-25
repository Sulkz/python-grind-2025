'''
Similar pattern as Merge Interval literally just add it to the ist
'''
class Solution(object):
    def insert(self, intervals, newInterval):
        #add the new intervakl to the list of lists
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
        
    
        