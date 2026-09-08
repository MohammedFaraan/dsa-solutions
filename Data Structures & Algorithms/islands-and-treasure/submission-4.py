class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        visit = set()
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        def addCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == -1:
                return
            
            visit.add((r, c))
            q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    addCell(r + dr, c + dc)

            dist += 1