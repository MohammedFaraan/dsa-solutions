class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        res = ""
        resLen = float("inf")

        countT = {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        need = len(countT)
        
        for i in range(len(s)):
            countS, curr = {}, 0
            for j in range(i, len(s)):
                ch = s[j]
                countS[ch] = 1 + countS.get(ch, 0)
                
                if ch in countT and countT[ch] == countS[ch]:
                    curr+=1
                
                if curr == need:
                    if (j-i+1) < resLen:
                        res=s[i:j+1]
                        resLen = (j-i+1)

        return res