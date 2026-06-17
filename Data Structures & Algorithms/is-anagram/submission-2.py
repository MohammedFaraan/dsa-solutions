class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = [0]*26

        for c in s:
            hashTable[ord("a") - ord(c)]+=1
        
        for c in t:
            hashTable[ord("a") - ord(c)]-=1
        
        for count in hashTable:
            if count != 0:
                return False

        return True