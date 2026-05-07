class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        
        s = "".join(chars)

        if s == s[::-1]:
            return True
        return False