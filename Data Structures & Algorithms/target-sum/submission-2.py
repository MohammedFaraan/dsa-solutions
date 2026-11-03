class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = dict()
        def dfs(i, curr_sum):
            if i == n:
                return 1 if curr_sum == target else 0

            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            dp[(i, curr_sum)] = dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])

            return dp[(i, curr_sum)]

        return dfs(0, 0)