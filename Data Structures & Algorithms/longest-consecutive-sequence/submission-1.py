class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
            
        nums.sort()
        maxLen = 0

        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i]-1 == nums[i-1]:
                count += 1
            else:
                maxLen = max(maxLen, count)
                count = 1
        
        maxLen = max(maxLen, count)
        return maxLen
