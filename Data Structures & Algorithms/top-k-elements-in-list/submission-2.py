class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = dict()

        for n in nums:
            numsMap[n] = numsMap.get(n, 0)+1
        
        res= sorted(numsMap, key=numsMap.get, reverse=True)

        return res[:k]