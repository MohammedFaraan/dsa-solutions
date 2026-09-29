from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        @cache
        def getMaxAmount(sub_nums: tuple, i: int) -> int:   
            # Base case: use the length of the current sub-list
            if i >= len(sub_nums):
                return 0

            # Choice 1: Rob current house and move to i+2
            # Choice 2: Skip current house and move to i+1
            return max(sub_nums[i] + getMaxAmount(sub_nums, i + 2), getMaxAmount(sub_nums, i + 1))
        
        rob_exclude_last = getMaxAmount(tuple(nums[:-1]), 0)
        rob_exclude_first = getMaxAmount(tuple(nums[1:]), 0)
        
        return max(rob_exclude_last, rob_exclude_first)
