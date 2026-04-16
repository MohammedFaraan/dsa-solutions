class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()

        for n in nums:
            if n in numSet:
                return n
            
            numSet.add(n)                                                                     