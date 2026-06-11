class Solution:
    def reverseBits(self, n: int) -> int:
        binaryCode = f"{n:032b}"

        return int(binaryCode[::-1], 2)
