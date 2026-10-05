class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(i, currSum):
            if currSum == amount:
                return 0

            if i >= len(coins) or currSum > amount:
                return float("inf")

            if dp[i][currSum] != -1:
                return dp[i][currSum]

            dp[i][currSum] = min(
                1 + dfs(i, currSum + coins[i]),
                dfs(i + 1, currSum)
            )

            return dp[i][currSum]

        res = dfs(0, 0)

        return res if res != float("inf") else -1