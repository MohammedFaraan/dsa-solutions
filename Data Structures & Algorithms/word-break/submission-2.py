class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [-1] * n

        def dfs(i):
            if i == n:
                return True

            if dp[i] != -1:
                return dp[i]

            res = False
            for j in range(i, n):
                if s[i : j + 1] in wordDict:
                    if dfs(j + 1):
                        res = True

            dp[i] = res
            return dp[i]

        return dfs(0)