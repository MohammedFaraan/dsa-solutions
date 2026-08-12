class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for p in points:
            dist = p[0]**2 + p[1]**2
            minHeap.append([dist, p[0], p[1]])

        heapq.heapify(minHeap)

        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
