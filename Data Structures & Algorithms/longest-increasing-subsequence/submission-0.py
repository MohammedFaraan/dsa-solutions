class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, prev):
            if i >= n:
                return 0

            # Shift prev by 1 to handle prev = -1
            if dp[i][prev + 1] != -1:
                return dp[i][prev + 1]

            # Option 1: Skip nums[i]
            res = dfs(i + 1, prev)

            # Option 2: Pick nums[i], if increasing
            if prev == -1 or nums[i] > nums[prev]:
                res = max(res, 1 + dfs(i + 1, i))

            dp[i][prev + 1] = res
            return res

        return dfs(0, -1)