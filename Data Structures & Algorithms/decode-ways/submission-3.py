class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1] * n

        def decodeWays(i):
            if i == n:
                return 1

            if memo[i] != -1:
                return memo[i]

            if s[i] == "0":
                memo[i] = 0
                return 0

            # Take one digit
            left = decodeWays(i + 1)

            # Take two digits if valid
            right = 0
            if i + 2 <= n and 10 <= int(s[i : i + 2]) <= 26:
                right = decodeWays(i + 2)

            memo[i] = left + right
            return memo[i]

        return decodeWays(0)