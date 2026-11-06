class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def dfs(r, c):
            if r >= n or c >= m:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            count = 0
            for dR, dC in directions:
                nR, nC = r + dR, c + dC
                if nR >= 0 and nR < n and nC >= 0 and nC < m and matrix[nR][nC] > matrix[r][c]:
                    count = max(count, 1 + dfs(nR, nC))
            
            dp[r][c] = count
            return dp[r][c]
        
        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, 1 + dfs(r, c))
        
        return res
