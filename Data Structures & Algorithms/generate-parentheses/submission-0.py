class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []

        def dfs(bracket, oCount, cCount, curr):
            if oCount > n or cCount > n:
                return
            
            if len(curr) == 2*n:
                temp.append("".join(curr))
                return
            
            curr.append(bracket)
            dfs("(", oCount+1, cCount, curr)
            
            curr.pop()
            dfs(")", oCount-1, cCount+1, curr)

        dfs("(", 0, 0, [])

        res = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        
        for b in temp:
            stack = []
            isValid = True
            for c in b:
                if c in {"}", "]", ")"}:
                    if stack and stack[-1] == closeToOpen[c]:
                        stack.pop()
                    else:
                        isValid = False
                else:
                    stack.append(c)
            
            if isValid and len(stack) == 0:
                res.append(b)
                
        return res