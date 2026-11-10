class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        def dfs(i, j):

            # If word1 is exhausted, insert all remaining
            # characters of word2.
            if i == n:
                return m - j

            # If word2 is exhausted, delete all remaining
            # characters of word1.
            if j == m:
                return n - i

            # Return cached result if this state was already computed.
            if dp[i][j] != -1:
                return dp[i][j]

            # If characters match, no operation is required.
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)

            else:
                # 1. Delete: Move forward in word1.
                delete = 1 + dfs(i + 1, j)

                # 2. Insert: Move forward in word2.
                insert = 1 + dfs(i, j + 1)

                # 3. Replace: Move forward in both strings.
                replace = 1 + dfs(i + 1, j + 1)

                # Choose the operation with minimum cost.
                res = min(delete, insert, replace)

            # Cache the minimum operations for this state.
            dp[i][j] = res
            return res

        return dfs(0, 0)