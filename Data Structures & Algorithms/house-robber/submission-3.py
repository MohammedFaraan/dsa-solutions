from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def getMaxAmount(i):
            if i >= n:
                return 0

            return max(nums[i] + getMaxAmount(i + 2), getMaxAmount(i + 1))

        return getMaxAmount(0)
