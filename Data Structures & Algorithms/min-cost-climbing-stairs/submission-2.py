class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        cache = [-1] * (len(cost))

        def getMinCost(n):
            if n <= 1:
                return cost[n]

            if cache[n] != -1:
                return cache[n]

            cache[n] = cost[n] + min(getMinCost(n - 1), getMinCost(n - 2))
            return cache[n]

        return getMinCost(len(cost) - 1)