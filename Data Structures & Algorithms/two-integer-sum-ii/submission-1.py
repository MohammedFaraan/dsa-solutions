class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        numsMap = {}

        for i in range(n):
            if target-numbers[i] in numsMap:
                return [numsMap[target-numbers[i]]+1, i+1]
            else:
                numsMap[numbers[i]] = i
        