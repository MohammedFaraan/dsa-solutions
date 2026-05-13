class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        countS1 = [0]*26
        countS2 = [0]*26

        for i in range(n1):
            countS1[ord(s1[i]) - ord("a")] += 1
            countS2[ord(s2[i]) - ord("a")] += 1

        for i in range(n2-n1):
            if countS1 == countS2:
                return True
            
            countS2[ord(s2[i]) - ord("a")] -= 1
            countS2[ord(s2[i+n1]) - ord("a")] += 1
        
        return countS1 == countS2