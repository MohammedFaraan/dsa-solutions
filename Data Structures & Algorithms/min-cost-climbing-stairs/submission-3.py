class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        cache = [0] * (len(cost))
        cache[0], cache[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            cache[i] = cost[i] + min(cache[i - 1], cache[i - 2])

        return cache[-1]