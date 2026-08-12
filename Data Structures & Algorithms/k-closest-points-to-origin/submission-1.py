class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for p in points:
            distances.append((math.sqrt(p[0]**2 + p[1]**2), p))

        heapq.heapify(distances)

        res = []

        while len(distances) > 0 and k > 0:
            res.append(heapq.heappop(distances)[1])
            k -= 1

        return res
