class Solution:
    def binary_search(self, nums, l, r, target):
        if l > r:
            return -1

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(nums, l, mid - 1, target)
        else:
            return self.binary_search(nums, mid + 1, r, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)