class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strsArr = []

        for c in s:
            if c.isalpha() or c.isnumeric():
                strsArr.append(c.lower())
        
        return strsArr == strsArr[-1::-1]