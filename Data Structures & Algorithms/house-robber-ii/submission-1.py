from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()

        @cache
        def getMaxAmount(i, robbed_first):   
            if (robbed_first and i >= n-1) or i >= n:
                return 0
            
            if i == 0:
                robbed_first = True
            left = nums[i] + getMaxAmount(i + 2 , robbed_first)

            if i == 0:
                robbed_first = False
            right = getMaxAmount(i + 1, robbed_first)
            return max(left, right)
        
        return getMaxAmount(0, False)
