class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1] * n

        def dfs(i):
            if i == n:
                return 1

            if memo[i] != -1:
                return memo[i]

            if s[i] == "0":
                memo[i] = 0
                return 0

            # Decode one digit
            res = dfs(i + 1)

            # Decode two digits
            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)

            memo[i] = res
            return res

        return dfs(0)