class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])
        
        res = 0
        visit = set()
        minHeap = [[0, 0]]

        while len(visit) < n:
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            res += cost
            visit.add(point)

            for neiCost, nei in adj_list[point]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])

        return res