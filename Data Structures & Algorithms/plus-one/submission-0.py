class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])

        sumStr = str(int("".join(digits)) + 1)
        res = [int(d) for d in sumStr]
        return res