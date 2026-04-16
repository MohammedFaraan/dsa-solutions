class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t in operators:
                num2 = nums.pop()
                num1 = nums.pop()

                res = 0

                if t == "+":
                    res = num1 + num2
                elif t == "-":
                    res = num1 - num2
                elif t == "*":
                    res = num1 * num2
                elif t == "/":
                    res = int(num1 / num2)

                nums.append(res)
            else:
                nums.append(int(t))

        return nums[0]
