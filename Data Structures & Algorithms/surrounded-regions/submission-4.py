class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            
            board[r][c] = "#"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        for r in [0, ROWS-1]:
            for c in range(COLS):
                if board[r][c] == "O":
                    capture(r, c)
        
        for c in [0, COLS-1]:
            for r in range(ROWS):
                if board[r][c] == "O":
                    capture(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
                        