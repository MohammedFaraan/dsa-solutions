class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n - 1):
            seen = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in seen:
                    res.add((nums[i], nums[j], third))
                
                seen.add(nums[j])
        
        return [list(triplets) for triplets in res]