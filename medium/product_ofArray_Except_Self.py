#PROBLEM TO DO WITH PREFIX PRODUCT AND SUFFIX CREATING A MULTIPLIER AND UPDATING THE ARRAY FIRST FROM LEFT TO RIGHT THEN FROM RIGHT TO LEFT 
#ALLOWING FOR THE PREFIX MULTIPLIER AND THEN THE SUFFIX MULTIPLER TO BE CALCULATED AND THEN APPLIED TO THE COPY ARRAY

class Solution(object):
    def productExceptSelf(self, nums):
        #initialise the pre and suf to 1 to allow multiplication to occur
        pre = 1
        suf = 1
        #initialise the array with 1s to allow multiplication and so its the size of the original
        arr = [] * len(nums)
        #first loop to achieve orefix multipliers and update arr
        for n in range(len(nums)):
            arr[n] = pre
            pre *= nums[n]
        #this loop goes backwards and calcs the suffix mult and then updates
        for i in range(len(nums) -1, -1,-1):
            arr[i] *= suf
            suf *= nums[i]
        return arr 