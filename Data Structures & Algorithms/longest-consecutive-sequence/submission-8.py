class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = {n for n in nums}
        maxLen = 0

        for n in numSet:
            if n-1 not in numSet:
                count = 1

                while n+count in numSet:
                    count += 1
                
                maxLen = max(maxLen, count)
        
        return maxLen
