"""
Maximum units on a truck
https://leetcode.com/problems/maximum-units-on-a-truck/
"""

def maximumUnits(boxTypes, truckSize):
    #sorts and puts the units into descending order for the greedy search
    boxTypes.sort(key=lambda box: box[1], reverse=True)
    totalUnits = 0
    #for 2d array can do each part like index [0,0] and [0,1]
    for boxes, units in boxTypes:
        if truckSize == 0:
            break
        picked_boxes = min(boxes,truckSize)
        totalUnits += (picked_boxes * units)
        # keeps track of Truckspace
        truckSize -= picked_boxes
    return totalUnits
        