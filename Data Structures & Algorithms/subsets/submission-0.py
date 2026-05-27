class Solution:
    def getAllSubsets(self, nums, res, i, allSubsets):
        if (i == len(nums)):
            allSubsets.append(res[:]) # res.copy or list(res)
            return

        # include
        res.append(nums[i])
        self.getAllSubsets(nums, res, i+1, allSubsets)

        # exclude
        res.pop() # backtracking
        self.getAllSubsets(nums, res, i+1, allSubsets)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        res = []
        
        self.getAllSubsets(nums, res, 0, allSubsets)

        return allSubsets
        