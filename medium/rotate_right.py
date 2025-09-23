class Solution(object):
    def rotate(self, nums, k):
        for _ in range(k):
            item = nums.pop()
            nums.insert(0,item)
        return nums