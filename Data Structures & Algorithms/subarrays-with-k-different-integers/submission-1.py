class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(k):
            count = defaultdict(int)
            res = l = 0

            for r in range(len(nums)):
                count[nums[r]] += 1
                if count[nums[r]] == 1:
                    k -= 1

                while k < 0:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        k += 1
                    l += 1

                res += (r - l + 1)

            return res

        return atMostK(k) - atMostK(k - 1)