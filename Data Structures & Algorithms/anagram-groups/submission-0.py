from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        anagrams = defaultdict(list)

        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        
        return list(anagrams.values())