class Solution(object):
    def findMaxConsecutiveOnes(nums):
        # another sliding door style problem but a simplier version
        count = 0
        max_length = 0
        # go through each value see if is one add to count if not reset the count
        for n in nums:
            if n == 1:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 0
        return max_length
    
    
    
print(Solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))