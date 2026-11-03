class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = dict()

        def dfs(i, t):
            if i == n and t == target:
                return 1

            if i >= n:
                return 0

            if (i, t) in dp:
                return dp[(i, t)]

            dp[(i, t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])

            return dp[(i, t)]

        return dfs(0, 0)
