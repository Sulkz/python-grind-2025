"""
Subarray Sums Divisible by K https://leetcode.com/problems/subarray-sums-divisible-by-k
"""

from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        #intialise the count and sum and result
        result = 0
        pre_sum = 0
        count = defaultdict(int)
        count[0] = 1
        
        for n in nums:
            pre_sum += n
            remainder = ((pre_sum % k) + k) % k
            if remainder in count:
                result += count[remainder]
            count[remainder] += 1
        return result