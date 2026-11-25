class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prev_height):
            if (
                (r, c) in visit
                or r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or heights[r][c] < prev_height
            ):
                return

            visit.add((r, c))
            for dR, dC in directions:
                dfs(r + dR, c + dC, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        return list(pacific.intersection(atlantic))