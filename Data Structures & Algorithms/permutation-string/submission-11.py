class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        countS1 = {}
        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1
        
        need = len(countS1)

        for i in range(n2):
            countS2, curr = {}, 0
            for j in range(i, n2):
                countS2[s2[j]] = countS2.get(s2[j], 0) + 1
                if countS1.get(s2[j], 0) < countS2[s2[j]]:
                    break
                
                if countS1[s2[j]] == countS2[s2[j]]:
                    curr += 1
                
                if curr == need:
                    return True
                
        return curr == need