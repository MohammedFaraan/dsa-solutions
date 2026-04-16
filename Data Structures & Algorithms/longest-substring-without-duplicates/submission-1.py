class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            hashSet = set()
            for j in range(i, n):
                if s[j] in hashSet:
                    break
                hashSet.add(s[j])
                res = max(res, len(hashSet))
        
        return res