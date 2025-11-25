from collections import Counter
import numpy as np


# # class Solution(object):
# #     def findLeastNumOfUniqueInts(arr,k):
# #         cnt = Counter(arr)
# #         freq = sorted(cnt.keys())
# #         for i in range(len(freq)):
# #             if k >= freq[i]:
# #                 k -= freq[i]
# #                 freq[i] = 0
# #             else:
# #                 freq[i] -= k
# #                 k = 0
# #                 break
# #         return sum(1 for f in freq if f > 0)
                
    
        
# # print(Solution.findLeastNumOfUniqueInts([5,5,4],1))


# def largest_two_digits_from_string(s):
#     maxim = -float("inf")
#     for x in range(len(s)-1):
#         nums = int(s[x:x+2])
#         maxim = max(maxim, nums)
#     return maxim


# # def getMinimumValue(data,maxOperations):
# #     bst_diff = float("inf")
# #     cnt = 0
    
# #     if not data:
# #         return 0
    
# #     if maxOperations == 0:
# #         return 0
# #     if maxOperations == 1:
# #         return min(data)
    
# #     for i in range(len(data)):
# #         for j in range (i+1, len(data)):
# #             diff = abs(data[i]-data[j])
# #             data.append(diff)
# #             print(data)
        
# #             cnt += 1
# #             if cnt > maxOperations:
# #                 break
# #     return min(data)

# import math
# from typing import Counter

# # def getMinimumValue(data, maxOperations):
# #     n = len(data)
# #     if maxOperations > 10 * n:
# #         return 0
# #     arr = data[:]
# #     for _ in range(maxOperations):
# #         arr.sort()
# #         min_diff = float('inf')
# #         for i in range(len(arr) - 1):
# #             diff = arr[i+1] - arr[i]
# #             if diff < min_diff:
# #                 min_diff = diff
# #         arr.append(min_diff)
# #     return min(arr)


# # print(getMinimumValue([0,9,8],1))
# def rotate(nums, k):
#     for _ in range(k):
#         item = nums.pop(0)
#         nums.append(item)
#     return nums
        


# class Solution:
#     def topKFrequent(self, nums, k: int):
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
        

# print(Solution.topKFrequent([1,2,2,3,3,3],1))

    
def concurrentSubarray(nums):

    if not nums:
        return 0

    current_len = 0

    for x in range (1, len(nums)):
        if nums[x] != nums[x -1]:
            current_len += 0
        else:
            current_len += 1

    return current_len

print(concurrentSubarray([1,1,1,1,1,0,1]))

def fleetTest():
    test = []
    num = 10
    print("we are testing this new app")
    test.append(num)
    return test

print(fleetTest())


def mean_standard_calc(nums):
    sums = 0
    for n in nums:
        sums += n
    mean = sums/len(nums)
    st_dv = np.std(nums, ddof=1)
    if mean >= (mean-(3*st_dv)) and mean <= (mean +(3*st_dv)):
        return f":0 we correct dawg in range {mean-(3*st_dv)} and {mean +(3*st_dv)} as mean is {mean} and standard {st_dv} "
    return f":0 we wrong dawg is not in range {mean-(3*st_dv)} and {mean +(3*st_dv)} as mean is {mean} and standard {st_dv} "
    

mean_standard_calc([42,47,59, 27, 84, 49, 72, 43, 73, 59, 58, 82, 50, 79,89, 75, 70, 59, 67, 35])


def wow(s: str):
    arr = []
    gang = s.split(" ")
    for word in gang:
        if len(word) <= 2:
            first = word.lower()
            arr.append(first)
            phrase = " ".join(arr)
        else:
            first = word.lower().capitalize()
            arr.append(first)
            phrase = " ".join(arr)
    return phrase

print(wow("First leTTeR of EACH Word"))


    
    