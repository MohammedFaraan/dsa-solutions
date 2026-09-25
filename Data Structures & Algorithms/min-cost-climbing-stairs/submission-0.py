from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        @cache
        def getMinCost(n):
            if n <= 1:
                return cost[n]
            
            return cost[n] + min(getMinCost(n-1), getMinCost(n-2))
        
        return getMinCost(len(cost) - 1)