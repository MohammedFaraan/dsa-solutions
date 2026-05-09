class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []

        for nums in matrix:
            for n in nums:
                res.append(n)
        
        l, h = 0, len(res)-1

        while l <= h:
            mid = (l+h) // 2

            if res[mid] == target:
                return True
            elif res[mid] > target:
                h = mid-1
            else:
                l = mid+1
        return False