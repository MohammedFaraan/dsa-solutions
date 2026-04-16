from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord("a")] += 1
            
            anagrams[tuple(count)].append(s)
            
        
        return list(anagrams.values())