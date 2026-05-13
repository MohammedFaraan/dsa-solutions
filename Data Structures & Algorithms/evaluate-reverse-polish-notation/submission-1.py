class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if t == "+":
                op2, op1 = nums.pop(), nums.pop()
                nums.append(op1 + op2)
            elif t == "-":
                op2, op1 = nums.pop(), nums.pop()
                nums.append(op1 - op2)
            elif t == "*":
                op2, op1 = nums.pop(), nums.pop()
                nums.append(op1 * op2)
            elif t == "/":
                op2, op1 = nums.pop(), nums.pop()
                nums.append(int(op1 / op2))
            else:
                nums.append(int(t))

        return nums[-1]