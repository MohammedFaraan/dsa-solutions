class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pwwkew
       res = 0
       l = 0
       for i in range(len(s)):
        set1 = set()
        for j in range(i, len(s)):
            if s[j] in set1:
                res = max(res, len(set1))
                break
            else:
                set1.add(s[j])
        res = max(res, len(set1))
        
       return res