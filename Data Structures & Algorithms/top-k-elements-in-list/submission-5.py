from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for n, freq in count.items():
            heapq.heappush(heap, [freq, n])

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [n for freq, n in heap]