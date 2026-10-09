class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [-1] * n

        def dfs(idx):
            if idx == n:
                return True
            if idx > n:
                return False

            if dp[idx] != -1:
                return dp[idx]

            res = False
            subStr = ""
            for i in range(idx, n):
                subStr += s[i]
                if subStr in wordDict:
                    if dfs(i + 1):
                        res = True
            
            dp[idx] = res
            return dp[idx]
        
        return dfs(0)