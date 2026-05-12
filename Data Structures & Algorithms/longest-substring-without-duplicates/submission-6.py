class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charSet = set()
        res = 0
        l = r = 0

        while r < n:
            while s[r] in charSet and l <= r:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, len(charSet))
            r += 1
        
        return res