class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: idx for idx, c in enumerate(order)}

        def compare(word):
            return [order_map[c] for c in word]

        return all(
            compare(words[i]) <= compare(words[i + 1]) for i in range(len(words) - 1)
        )