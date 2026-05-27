class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return

            # include
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            idx = i + 1

            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1

            # exclude
            dfs(idx)

        dfs(0)

        return res
