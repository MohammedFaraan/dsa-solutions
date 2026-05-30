class Solution:
    def getCombinationSum(self, nums, idx, subset, target):
        if target == 0:
            self.res.append(subset[:])
            return
        if target < 0:
            return
        if idx == len(nums):
            return
        
        subset.append(nums[idx])
        self.getCombinationSum(nums, idx, subset, target - nums[idx])

        subset.pop()
        self.getCombinationSum(nums, idx+1, subset, target)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        self.getCombinationSum(nums, 0, [], target)

        return self.res
        