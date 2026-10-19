class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][j + 1] stores the maximum profit starting from day i,
        # where j is the day we bought the stock.
        # j = -1 means we currently have no stock to sell.
        dp = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            # No days left to make a transaction
            if i >= n:
                return 0

            # Return the cached result if this state was already computed
            if dp[i][j + 1] != -1:
                return dp[i][j + 1]

            res = 0

            if j == -1:
                # Option 1: Buy today
                # Option 2: Skip today
                res = max(
                    dfs(i + 1, i),
                    dfs(i + 1, -1)
                )
            else:
                # Option 1: Sell today if the price is higher than the buy price
                if prices[i] > prices[j]:
                    profit = prices[i] - prices[j]

                    # After selling, skip the next day due to cooldown
                    res = profit + dfs(i + 2, -1)

                # Option 2: Keep holding the stock and consider selling later
                res = max(res, dfs(i + 1, j))

            # Cache the result using the shifted index
            dp[i][j + 1] = res
            return res

        # Start on day 0 without owning a stock
        return dfs(0, -1)