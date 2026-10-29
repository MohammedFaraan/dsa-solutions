class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def getWays(n):
            if n <= 2:
                return n

            if dp[n] != -1:
                return dp[n]

            dp[n] = getWays(n - 1) + getWays(n - 2)
            return dp[n]

        return getWays(n)