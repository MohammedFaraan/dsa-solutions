class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            onesCount = bin(i).count("1")
            res.append(onesCount)

        return res
