class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def dfs(i, buying):
            if i >= n:
                return 0
            
            if dp[i][buying] != -1:
                return dp[i][buying]
            
            if buying:
                buy = dfs(i + 1, 0) - prices[i]
                skip = dfs(i + 1, 1)

                dp[i][buying] = max(buy, skip)
            else:
                sell = prices[i] + dfs(i + 2, 1)
                hold = dfs(i + 1, 0)

                dp[i][buying] = max(sell, hold)
            
            return dp[i][buying]
        
        return dfs(0, 1)
