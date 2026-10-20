
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Two states per day: buying or holding a stock
        dp = [[-1] * 2 for _ in range(n)]

        def dfs(i, buying):
            # No days left
            if i >= n:
                return 0

            # Return cached result
            if dp[i][buying] != -1:
                return dp[i][buying]

            if buying:
                # Option 1: Buy today
                buy = dfs(i + 1, 0) - prices[i]

                # Option 2: Skip today
                skip = dfs(i + 1, 1)

                dp[i][buying] = max(buy, skip)
            else:
                # Option 1: Sell today; next day is cooldown
                sell = prices[i] + dfs(i + 2, 1)

                # Option 2: Keep holding the stock
                hold = dfs(i + 1, 0)

                dp[i][buying] = max(sell, hold)

            return dp[i][buying]

        return dfs(0, 1)
