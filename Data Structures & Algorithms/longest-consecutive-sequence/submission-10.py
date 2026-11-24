class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for n in numSet:
            if n - 1 not in numSet:
                cnt = 0
                while n + cnt in numSet:
                    cnt += 1
                
                maxLen = max(maxLen, cnt)
        
        return maxLen