class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, sums):
            if sums == target:
                res.append(subset.copy())
                return
            
            if i == len(nums) or sums > target:
                return
            
            subset.append(nums[i])
            dfs(i, sums + nums[i])

            subset.pop()
            dfs(i + 1, sums)
        
        dfs(0, 0)

        return res
            
        