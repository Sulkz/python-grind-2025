class Solution(object):
    def merge(intervals):
        #sorting the first integer of each interval in the list
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            #if the last items last element placed in merged is smaller than the first item in interal then its fine no need change
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                #checks last element of each interval and replaces with the larger amount
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged
print(Solution.merge([[1,3],[2,6],[8,10],[15,18]]))
                
        