class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions =[[0, -1], [0, 1], [-1, 0], [1, 0]]
        max_area = 0
        area = 0

        def dfs(r, c):
            nonlocal area
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return
            area += 1

            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
                    max_area = max(max_area, area)
        return max_area