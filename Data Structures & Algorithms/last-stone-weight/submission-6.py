class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first, second = heapq.heappop_max(stones), heapq.heappop_max(stones)
            
            if first != second:
                heapq.heappush_max(stones, first - second)
        
        return stones[0] if stones else 0