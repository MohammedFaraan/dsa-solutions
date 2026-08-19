class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = dict()
        for idx, c in enumerate(order):
            order_map[c] = idx

        for i in range(1, len(words)):
            min_len = min(len(words[i - 1]), len(words[i]))
            j = 0
            while j < min_len:
                left = order_map[words[i - 1][j]]
                right = order_map[words[i][j]]

                if left < right:
                    break

                if left > right:
                    return False

                j += 1

            if j == min_len and len(words[i - 1]) > len(words[i]):
                return False

        return True