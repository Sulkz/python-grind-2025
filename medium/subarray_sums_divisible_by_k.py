"""
Subarray Sums Divisible by K https://leetcode.com/problems/subarray-sums-divisible-by-k
"""





from collections import defaultdict


class Solution(object):
    def subarraysDivByK(self, nums, k):
        #intialise the count and sum and result
        res = 0
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        
        # loop through each number in nums  using them as the endings of a subarray
        for n in nums:
            prefix_sum += n #caslcualtes the prefix sum
            remainder = ((prefix_sum % k) + k) % k #this accounts for negative numbers in the subarry
            
            if remainder in count:
                res += count[remainder]
            count[remainder] += 1
        return res
        