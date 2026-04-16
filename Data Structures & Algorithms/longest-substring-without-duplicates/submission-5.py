class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0

        i, j = 0, 0
        hashSet = set()

        while j < n:
            while i<j and s[j] in hashSet:
                hashSet.remove(s[i])
                i+=1

            hashSet.add(s[j])
            res = max(res, len(hashSet))
            j+=1
        
        return res