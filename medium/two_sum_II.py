class Solution:
    def twoSum(nums, target):
        #srted 
        #brute force solution
        # for x in range(len(nums)):
        #     for y in range(x+1, len(nums)):
        #         if nums[x] + nums[y] == target:
        #             return [x +1, y+1]
        # return []

        #optimal solution - Two pointer
        l, r = 0, len(nums)-1
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
            if curSum < target:
                l += 1
            if curSum == target:
                return [l+1,r+1]
print(Solution.twoSum([2,5,7,9,11],12))
        
        
        