class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i, j):
            if i == m and j == n:
                return True

            if dp[i][j] != -1:
                return dp[i][j]

            k = i + j
            res = False
            if i < m and s1[i] == s3[k]:
                res = dfs(i + 1, j)

            if not res and j < n and s2[j] == s3[k]:
                res = dfs(i, j + 1)

            dp[i][j] = res
            return dp[i][j]

        return dfs(0, 0)
