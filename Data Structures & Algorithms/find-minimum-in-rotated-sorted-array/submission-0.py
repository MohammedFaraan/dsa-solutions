class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < res:
                res = nums[mid]

            if nums[l] <= nums[mid]:
                if nums[r] < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return res
