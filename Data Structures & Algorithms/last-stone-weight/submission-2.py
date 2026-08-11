class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            n1, n2 = heapq.heappop_max(stones), heapq.heappop_max(stones)

            diff = n1 - n2

            heapq.heappush_max(stones, diff)
            
        return stones[0]