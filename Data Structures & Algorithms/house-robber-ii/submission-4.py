class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def rob_range(start, end):
            memo = [-1] * n

            def dfs(i):
                if i > end:
                    return 0

                if memo[i] != -1:
                    return memo[i]

                memo[i] = max(
                    nums[i] + dfs(i + 2),
                    dfs(i + 1)
                )
                return memo[i]

            return dfs(start)

        if n == 1:
            return nums[0]

        return max(
            rob_range(0, n - 2),
            rob_range(1, n - 1)
        )