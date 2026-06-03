class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        curr = []
        res = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(curr))
                return

            if open_count < n:
                curr.append("(")
                backtrack(open_count + 1, closed_count)
                curr.pop()

            if closed_count < open_count:
                curr.append(")")
                backtrack(open_count, closed_count + 1)
                curr.pop()

        backtrack(0, 0)
        return res