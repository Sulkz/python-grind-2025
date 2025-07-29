class Solution(object):
    def nextPermutation(nums):
        #first we want to initialise a pointer starting at the end of the array
        rp = len(nums) -1
        #then the first condition we looking for is the first decreasing number
        while rp > 0 and nums[rp-1] >= nums[rp]:
            rp -= 1
        #if the list is in decending order reverse the list
        if rp == 0:
            nums.reverse()
            return
        #requires a new pointer to then allow for swaping 
        j = len(nums) -1
    
        while j >= rp and nums[j] <= nums[rp-1]:
            j -= 1
        
        nums[rp-1],nums[j] = nums[j],nums[rp-1]
        nums[rp:] = reversed(nums[rp:])
        
        
print(Solution.nextPermutation([1,2,3]))