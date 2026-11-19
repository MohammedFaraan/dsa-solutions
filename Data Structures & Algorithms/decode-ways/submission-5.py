class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n

        def dfs(i):
            if i == n:
                return 1
            
            if dp[i] != -1:
                return dp[i]
            
            if s[i] == "0":
                dp[i] = 0
                return 0
            
            # decode 1 digit
            res = dfs(i + 1)

            if i + 1 < n and 10 <= int(s[i: i + 2]) <= 26:
                res += dfs(i + 2)
            
            dp[i] = res
            return dp[i]
        
        return dfs(0)