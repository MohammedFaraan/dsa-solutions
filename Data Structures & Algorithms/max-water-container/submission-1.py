class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxCapacity = 0

        while l < r:
            h = min(heights[l], heights [r])
            w = r - l
            capacity = h * w
            maxCapacity = max(maxCapacity, capacity)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxCapacity