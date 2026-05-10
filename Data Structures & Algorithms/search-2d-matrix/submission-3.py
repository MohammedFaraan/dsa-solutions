class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1

        while l <= h:
            mid = (l + h) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return self.binarySearch(matrix[mid], 0, len(matrix[mid]) - 1, target)
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                h = mid - 1

        return False

    def binarySearch(self, nums, l, h, t):
        while l <= h:
            m = (l + h) // 2

            if nums[m] == t:
                return True
            elif nums[m] > t:
                h = m - 1
            else:
                l = m + 1

        return False
