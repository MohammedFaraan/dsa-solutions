class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)

        for i in range(n):
            for j in range(i, n):
                if sorted(s2[i:j+1]) == sorted(s1):
                    return True
        
        return False