from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, j):
            if i >= n or j >= n:
                return 0
            
            res = 0
            if j != -1:
                if prices[i] > prices[j]:
                    profit = prices[i] - prices[j]
                    res = profit + dfs(i + 2, -1)
                
                res = max(res, dfs(i + 1, j))
            else:
                res = max(dfs(i + 1, i), dfs(i + 1, j))
        
            return res
        
        return dfs(0, -1)