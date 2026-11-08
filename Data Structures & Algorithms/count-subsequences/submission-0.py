class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        def dfs(i, j):
            if j == m:
                return 1
            
            if i >= n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            res += dfs(i + 1, j)

            dp[i][j] = res
            return res
        
        return dfs(0, 0)