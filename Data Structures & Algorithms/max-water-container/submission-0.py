class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxWater = 0
        i, j = 0, n - 1
        while i < j:
            w = j - i
            h = min(heights[i], heights[j])
            water = w * h
            maxWater = max(maxWater, water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxWater