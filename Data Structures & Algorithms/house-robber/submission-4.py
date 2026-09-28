from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        
        def getMaxAmount(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i] + getMaxAmount(i + 2), getMaxAmount(i + 1))
            return dp[i]

        res = getMaxAmount(0)

        return res
