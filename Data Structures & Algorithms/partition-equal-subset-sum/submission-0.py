class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)

        if len(nums) == 1:
            return False

        total = sum(nums)
        if total % 2 == 1:
            return False

        reqSum = total // 2
        dp = [[-1] * (reqSum + 1) for _ in range(n)]

        def dfs(i, s):
            if s == reqSum:
                return 1

            if i >= n or s > reqSum:
                return 0

            if dp[i][s] != -1:
                return dp[i][s]

            dp[i][s] = dfs(i + 1, s + nums[i]) + dfs(i + 1, s)
            return dp[i][s]

        return dfs(0, 0) > 0