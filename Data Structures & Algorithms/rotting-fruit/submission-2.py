class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        vist = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    vist.add((r, c))
        
        def addCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in vist:
                return
            
            grid[r][c] = -1
            q.append([r, c])
            vist.add((r, c))

        minutes = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                addCell(r, c - 1)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r + 1, c)
            
            minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return minutes if minutes > 0 else 0
 
