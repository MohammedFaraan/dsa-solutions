class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = []

        for i in range(n):
            sum = 1
            for j in range(n):
                if i != j:
                    sum *= nums[j]

            res.append(sum)

        return res
