class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * n for _ in range(amount + 1)]

        def dfs(amount, i):
            if amount == 0:
                return 1

            if dp[amount][i] != -1:
                return dp[amount][i]

            res = 0
            for j in range(i, n):
                if amount - coins[j] >= 0:
                    res += dfs(amount - coins[j], j)

            dp[amount][i] = res
            return res

        return dfs(amount, 0)