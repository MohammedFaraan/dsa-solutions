class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n, f in freq.items():
            if f == 1:
                return n