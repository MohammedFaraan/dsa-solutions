class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = [0] * 26

        for c in s:
            hashTable[ord(c) - ord("a")] += 1

        for c in t:
            hashTable[ord(c) - ord("a")] -= 1

        for count in hashTable:
            if count != 0:
                return False

        return True