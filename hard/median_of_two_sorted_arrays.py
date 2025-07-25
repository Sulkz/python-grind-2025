"""
Using Brute forec that does it in 2ms ! :0
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        median = 0
    
        # merging the lists and sorting
        nums1.extend(nums2)
        nums1.sort()
        
        #finding the postion of the median number
        
        e = int(len(nums1)/2)
        
        if len(nums1) % 2 == 0:
            median = float(nums1[e] + nums1[e-1])
        else:
            median = nums1[e]
        return median
        