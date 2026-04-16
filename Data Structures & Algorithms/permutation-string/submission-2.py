class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        l = 0

        countS1 = [0] * 26
        
        for ch in s1:
            countS1[ord(ch) - ord("a")] += 1
        
        countS2 = [0] * 26
        for r in range(len(s2)):
            countS2[ord(s2[r]) - ord("a")] += 1

            if (r-l+1) > n:
                countS2[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if countS1 == countS2:
                return True
            
        return False