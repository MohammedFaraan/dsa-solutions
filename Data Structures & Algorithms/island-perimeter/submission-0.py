class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cols = len(grid)
        rows = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i >= cols or j >= rows or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in visited:
                return 0
            
            visited.add((i, j))

            perim = dfs(i, j - 1) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j)

            return perim

        for i in range(cols): 
            for j in range(rows):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0 