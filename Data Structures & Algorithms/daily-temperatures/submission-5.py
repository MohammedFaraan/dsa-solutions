class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                pTemp, pIdx = stack.pop()
                res[pIdx] = idx - pIdx
            
            stack.append([temp, idx])

        return res
