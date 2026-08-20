class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return
            if (i, j) in visited:
                return

            visited.add((i, j))

            dfs(i, j - 1)
            dfs(i - 1 , j)
            dfs(i, j + 1)
            dfs(i + 1 , j)
        
        island_cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    print(i, j)
                    island_cnt += 1
                    dfs(i, j)

        return island_cnt