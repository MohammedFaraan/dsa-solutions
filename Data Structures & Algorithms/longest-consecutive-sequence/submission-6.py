class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        if len(nums) == 1:
            return 1
        maxCount = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                count += 1
            else:
                count = 1
            maxCount = max(maxCount, count)

        return maxCount
