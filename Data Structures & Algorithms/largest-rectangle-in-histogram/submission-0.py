class Solution:
        def largestRectangleArea(self, heights: List[int]) -> int:
            res = heights[0]
            n = len(heights)

            for i in range(n):
                minHeight = heights[i]
                for j in range(i + 1, n):
                    minHeight = min(minHeight, heights[j])
                    area = minHeight * (j - i + 1)

                    res = max(res, area)
                    
                res=max(res, heights[i])
            
            return res

                                                                                                                