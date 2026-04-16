class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        
        stack = []
        brackets = {"[": "]", "{": "}", "(": ")"}

        for ch in s:
            if ch == "]" or ch == "}" or ch == ")":
                if not stack or ch != brackets[stack.pop()]:
                    return False

            else:
                stack.append(ch)

        return True if not stack else False
