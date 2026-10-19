class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * n for _ in range(n)]

        def dfs(i, j):
            if i >= n or j >= n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            res = 0
            if j != -1:
                if prices[i] > prices[j]:
                    profit = prices[i] - prices[j]
                    res = profit + dfs(i + 2, -1)
                
                res = max(res, dfs(i + 1, j))
            else:
                res = max(dfs(i + 1, i), dfs(i + 1, j))
        
            dp[i][j] = res
            return dp[i][j]
        
        return dfs(0, -1)