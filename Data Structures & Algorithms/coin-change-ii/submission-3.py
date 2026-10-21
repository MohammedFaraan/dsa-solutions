class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # dp[i][amount] stores the number of combinations
        # to make 'amount' using coins from index i onward.
        dp = [[-1] * (amount + 1) for _ in range(n)]

        # Sort coins so we can stop considering larger coins
        # once the current coin exceeds the remaining amount.
        coins.sort()

        def dfs(i, amount):
            # If the remaining amount is 0, we found one valid combination.
            if amount == 0:
                return 1

            # If no coins remain and the amount is still positive,
            # there are no valid combinations.
            if i >= n:
                return 0

            # Return the cached result if this state was already computed.
            if dp[i][amount] != -1:
                return dp[i][amount]

            res = 0

            # Use the current coin only if it does not exceed the remaining amount.
            if amount >= coins[i]:

                # Choice 1: Take/Use the current coin.
                # Keep index i unchanged because the same coin can be reused.
                res = dfs(i, amount - coins[i])

                # Choice 2: Skip the current coin and move to the next one.
                # This avoids counting different orders of the same combination.
                res += dfs(i + 1, amount)

            # Cache the result for the current state.
            dp[i][amount] = res
            return res

        # Start with the first coin and the full target amount.
        return dfs(0, amount)