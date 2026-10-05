class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        def dfs(amount):
            if amount == 0:
                return 0

            if dp[amount] != -1:
                return dp[amount]

            res = float("inf")

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            dp[amount] = res
            return dp[amount]

        minCoins = dfs(amount)

        return -1 if minCoins == float("inf") else minCoins
