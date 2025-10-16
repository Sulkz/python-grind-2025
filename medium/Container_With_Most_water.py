class Solution:
    def maxArea(heights) -> int:
        l, r = 0, len(heights) -1
        area = 0
        while l < r:
            maxH = min(heights[l],heights[r])
            width = abs(r-l)
            area = max(area,(maxH*width))
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area
            
print(Solution.maxArea([2,2,2]))