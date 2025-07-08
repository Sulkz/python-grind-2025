class Solution(object):
    def minSubArrayLen(target, nums):
        # this problem will require a window that shrinks to find the sum that is equal to or greater than the target
        lf_side = 0
        min_length = float("inf")
        #we need to keep track of sum
        total = 0
        # run through the array 
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                min_length = min(min_length,i - lf_side + 1)
                total -= nums[lf_side]
                lf_side += 1
        return min_length if min_length != float("inf") else 0
    
    
print(Solution.minSubArrayLen(7,[2,3,1,2,4,3]))
    
   