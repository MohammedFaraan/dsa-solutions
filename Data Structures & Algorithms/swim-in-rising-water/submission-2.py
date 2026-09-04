class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiR == N
                    or neiC < 0
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    continue

                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])
