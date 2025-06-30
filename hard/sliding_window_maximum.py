"""
Brute force tactic
"""

class Solution(object):
    def maxSlidingWindow(nums, k):
        results = []
        for x in range(len(nums) - k + 1):
            # the openeing and closing has been set fot the window and the -1 deals with the index 0 
            y = x + k - 1
            window_max = max(nums[x:y + 1])
            results.append(window_max)
        return results
    
print(Solution.maxSlidingWindow([1,2,3,-1,1,3,4], 3))
            