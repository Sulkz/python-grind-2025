# from collections import Counter


# class Solution(object):
#     def findLeastNumOfUniqueInts(arr,k):
#         cnt = Counter(arr)
#         freq = sorted(cnt.keys())
#         for i in range(len(freq)):
#             if k >= freq[i]:
#                 k -= freq[i]
#                 freq[i] = 0
#             else:
#                 freq[i] -= k
#                 k = 0
#                 break
#         return sum(1 for f in freq if f > 0)
                
    
        
# print(Solution.findLeastNumOfUniqueInts([5,5,4],1))


def largest_two_digits_from_string(s):
    maxim = -float("inf")
    for x in range(len(s)-1):
        nums = int(s[x:x+2])
        maxim = max(maxim, nums)
    return maxim


# def getMinimumValue(data,maxOperations):
#     bst_diff = float("inf")
#     cnt = 0
    
#     if not data:
#         return 0
    
#     if maxOperations == 0:
#         return 0
#     if maxOperations == 1:
#         return min(data)
    
#     for i in range(len(data)):
#         for j in range (i+1, len(data)):
#             diff = abs(data[i]-data[j])
#             data.append(diff)
#             print(data)
        
#             cnt += 1
#             if cnt > maxOperations:
#                 break
#     return min(data)

import math
from typing import Counter

# def getMinimumValue(data, maxOperations):
#     n = len(data)
#     if maxOperations > 10 * n:
#         return 0
#     arr = data[:]
#     for _ in range(maxOperations):
#         arr.sort()
#         min_diff = float('inf')
#         for i in range(len(arr) - 1):
#             diff = arr[i+1] - arr[i]
#             if diff < min_diff:
#                 min_diff = diff
#         arr.append(min_diff)
#     return min(arr)


# print(getMinimumValue([0,9,8],1))
def rotate(nums, k):
    for _ in range(k):
        item = nums.pop(0)
        nums.append(item)
    return nums
        

# print(rotate([1,2,3,4,5,6,7],3))
# import numpy as np
# grade = np.array([10,20,90])
# high_grd = np.array([True,False,True])
# print(grade[~high_grd])
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frq = [[] for i in range(len(nums) + 1)]
#         count  = {}
#         res =[]
#         for n in nums:
#             count[n] = 1 + count.get(n,0)
#         for n, c in count.items():
#             frq[c].append(n)
#         for x in range(len(nums)-1,0,-1):
#             for i in frq[x]:
#                 res.append(i)
#                 if len(res) == k:
#                     return res
        
# print(topKFrequent([1,2,2,3,3,3],1))
nums = [1,2,3,4]
arr = [1] * len(nums)
print(arr)

    
