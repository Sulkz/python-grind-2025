"""
Problem: Two Sum
Difficulty: Easy
Approach 1: Brute Force (O(n^2))
Approach 2: Hash Map (O(n))

LeetCode link: https://leetcode.com/problems/two-sum/
"""

def two_sum(nums, target):
    # Brute force
    for x in range(0, len(nums)):
        for y in range(x+1,len(nums)):
            if(nums[x] +nums[y] == target):
                return [x,y]
    return[]

def two_sum_optimized(nums, target):
    # Hashmap
    hashmap = {}
    for x in range(0,len(nums)):
        complement = target - nums[x]
        if complement in hashmap:
            return [hashmap[complement], x]
        hashmap[nums[x]] = x
    return[]