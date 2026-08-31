class Solution:
    def isHappy(self, n: int) -> bool:
        seen_res = set()

        while n != 1:
            if n in seen_res:
                return False

            seen_res.add(n)

            curr_sum = 0
            while n > 0:
                digit = n % 10
                curr_sum += digit**2
                n //= 10

            n = curr_sum

        return True