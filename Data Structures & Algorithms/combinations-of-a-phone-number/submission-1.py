class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        keypad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        curr = []

        def getAllLetterComb(i):
            if i == len(digits):
                res.append("".join(curr))
                return
            
            chars = keypad[digits[i]]
            for ch in chars:
                curr.append(ch)
                getAllLetterComb(i+1)
                curr.pop()
        
        getAllLetterComb(0)
        return res