class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        numsMap = {nums[i]:i for i in range(n)}     
        nums.sort()

        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return numsMap[nums[mid]]
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        return -1