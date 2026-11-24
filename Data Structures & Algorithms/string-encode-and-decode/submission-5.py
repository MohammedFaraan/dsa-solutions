class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}${s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decodedStrList = []
        i = 0

        while i < len(s):
            sLen = ""
            while s[i] != "$":
                sLen += s[i]
                i += 1

            sLen = int(sLen)
            startIndex = i + 1
            i = startIndex + sLen

            decodedStrList.append(s[startIndex: i])

        return decodedStrList