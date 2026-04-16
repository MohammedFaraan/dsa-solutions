class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n=len(nums)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        threeSum=[nums[i],nums[j],nums[k]]
                        ans.add(tuple(sorted(threeSum)))

        return [list(arr) for arr in ans]