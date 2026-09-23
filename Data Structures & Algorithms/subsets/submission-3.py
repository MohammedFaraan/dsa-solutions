class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)

        def generateSubsets(idx):
            if idx == n:
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            generateSubsets(idx + 1)

            subset.pop()
            generateSubsets(idx + 1)
        

        generateSubsets(0)

        return res
        