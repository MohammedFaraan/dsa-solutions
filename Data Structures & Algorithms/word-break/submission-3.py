class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return True

            if dp[i] != -1:
                return dp[i]

            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        dp[i] = True
                        return True

            dp[i] = False
            return False

        return dfs(0)