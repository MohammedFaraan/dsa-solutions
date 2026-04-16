class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        if s == t:
            return s

        minStr = ""

        countT = {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        n=len(s)
        need = len(countT)
        
        for i in range(n):
            countS, curr = {}, 0
            for j in range(i, n):
                countS[s[j]] = 1 + countS.get(s[j], 0)
                
                if countT.get(s[j], 0)==countS[s[j]]:
                    curr+=1
                
                if curr == need:
                    subStr=s[i:j+1]
                    if len(minStr)==0:
                        minStr=subStr
                    elif len(minStr)>len(subStr):
                        minStr=subStr

        return minStr