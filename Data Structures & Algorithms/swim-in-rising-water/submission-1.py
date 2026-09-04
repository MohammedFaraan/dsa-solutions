class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        adj_list = defaultdict(list)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                        continue
                    
                    adj_list[(r, c)].append((row, col))
        
        minHeap = [[grid[0][0], (0, 0)]]
        visit = set()
        res = 0
        while minHeap:
            t, sq = heapq.heappop(minHeap)
            if sq in visit:
                continue
            res = max(res, t)
            visit.add(sq)
            if sq == (ROWS-1, COLS-1):
                return res
            
            for r, c in adj_list[sq]:
                if (r, c) not in visit:
                    heapq.heappush(minHeap, [grid[r][c], (r, c)])

        return res     