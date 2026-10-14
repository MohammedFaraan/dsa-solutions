import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range for eating speed 'k'
        l, r = 1, max(piles)
        res = r  # The maximum pile size is always a valid answer

        def calcTotalHours(k):
            totalH = 0
            for p in piles:
                totalH += math.ceil(p / k)
            return totalH

        while l <= r:
            mid = (l + r) // 2
            totalH = calcTotalHours(mid)

            if totalH <= h:
                res = mid      # mid is valid, but let's check if a smaller speed works
                r = mid - 1
            else:
                l = mid + 1    # Koko is too slow, we need a faster speed
        
        return res