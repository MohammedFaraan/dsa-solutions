class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            c1, c2 = s[l], s[r]
            if not c1.isalnum():
                l+=1
            elif not c2.isalnum():
                r-=1
            else:
                if c1.lower() != c2.lower():
                    return False
                l+=1; r-=1
        
        return True