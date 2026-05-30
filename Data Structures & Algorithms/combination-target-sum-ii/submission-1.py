class Solution:
    def getCombinationSum(self, candidates, idx, subset, target):
        if target == 0:
            self.res.append(subset[:])
            return
        if target < 0:
            return
        if idx >= len(candidates):
            return

        subset.append(candidates[idx])
        self.getCombinationSum(candidates, idx+1, subset, target - candidates[idx])

        subset.pop()
        i = idx + 1
        while i < len(candidates) and candidates[i] == candidates[i-1]:
            i += 1
        self.getCombinationSum(candidates, i, subset, target)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []

        self.getCombinationSum(candidates, 0, [], target)

        return self.res