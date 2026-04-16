class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLen = 0

        for num in numSet:
            curr, count = num, 0

            while curr in numSet:
                count+=1
                curr += 1
            
            maxLen = max(maxLen, count)
        
        return maxLen