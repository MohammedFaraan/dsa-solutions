from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache
        def decodeWays(i):
            if i == n:
                return 1

            if s[i] == "0":
                return 0

            left = decodeWays(i + 1)

            right = (
                decodeWays(i + 2)
                if i + 2 <= n and int(s[i:i + 2]) <= 26
                else 0
            )

            return left + right

        return decodeWays(0)