from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def count_combinations(curr_sum):
            if curr_sum == n:
                return 1
            if curr_sum > n:
                return 0

            return count_combinations(curr_sum + 1) + count_combinations(curr_sum + 2)
        return count_combinations(0)