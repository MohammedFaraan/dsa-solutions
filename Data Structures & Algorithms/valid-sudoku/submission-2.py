class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for r in range(n):
            seen = set()
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for c in range(n):
            seen = set()
            for r in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (square // 3) * 3 + i
                    c = (square % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])

        return True
