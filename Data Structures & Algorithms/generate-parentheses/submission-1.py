class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def dfs(open_count, close_count, curr):
            # Base case: valid combination found
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return
            
            # Decision 1: Only add '(' if we haven't reached the limit 'n'
            if open_count < n:
                curr.append("(")
                dfs(open_count + 1, close_count, curr)
                curr.pop() # Backtrack
                
            # Decision 2: Only add ')' if it closes a matching '('
            if close_count < open_count:
                curr.append(")")
                dfs(open_count, close_count + 1, curr)
                curr.pop() # Backtrack

        dfs(0, 0, [])
        return res
