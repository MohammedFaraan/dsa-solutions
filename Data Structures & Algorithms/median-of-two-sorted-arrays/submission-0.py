class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 == 0:
            return self.binarySearch(nums2, 0, n2 - 1, n2)
        elif n2 == 0:
            return self.binarySearch(nums1, 0, n1 - 1, n1)

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        if i < n1:
            nums.extend(nums1[i:])
        elif j < n2:
            nums.extend(nums2[j:])

        return self.binarySearch(nums, 0, len(nums) - 1, len(nums))

    def binarySearch(self, nums, l, r, n):
        if n == 0:
            return 0
        m = (l + r) // 2
        sum = 0
        if n % 2 == 0:
            sum = nums[m] + nums[m + 1]
            return sum / 2
        else:
            sum = nums[m]
            return sum
