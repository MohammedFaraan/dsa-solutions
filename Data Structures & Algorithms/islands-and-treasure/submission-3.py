class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        visit = set()
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = min(grid[r][c], dist)
                if (r, c) in visit:
                    continue
                visit.add((r, c))
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] in [0, -1]):
                        continue
                    q.append((row, col))
            
            dist += 1 