class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            n1, n2 = stones.pop(), stones.pop()
            diff = n1 - n2

            if diff > 0:
                stones.append(diff)
                stones.sort()

        return stones[0] if stones else 0