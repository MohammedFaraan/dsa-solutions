class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        first_seen = {0: -1}
        res = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                balance += 1
            else:
                balance -= 1

            if balance in first_seen:
                res = max(res, i - first_seen[balance])
            else:
                first_seen[balance] = i

        return res