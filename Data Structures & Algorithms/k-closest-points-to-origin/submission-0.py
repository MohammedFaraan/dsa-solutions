class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            distances.append((math.sqrt(x**2 + y**2), points[i]))

        heapq.heapify(distances)

        res = []

        while len(distances) > 0 and k > 0:
            res.append(heapq.heappop(distances)[1])
            k -= 1

        return res
