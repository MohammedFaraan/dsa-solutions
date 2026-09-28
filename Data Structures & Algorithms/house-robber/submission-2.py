from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAmount = 0
        n = len(nums)

        @cache
        def getMaxAmount(i, amount):
            nonlocal maxAmount
            if i >= n:
                maxAmount = max(maxAmount, amount)
                return
            
            getMaxAmount(i + 2, amount + nums[i])

            getMaxAmount(i + 1, amount)
        
        getMaxAmount(0, 0)

        return maxAmount
