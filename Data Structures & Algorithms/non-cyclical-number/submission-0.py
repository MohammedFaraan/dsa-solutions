class Solution:
    def isHappy(self, n: int) -> bool:
        res = [str(n)]

        while True:
            curr_sum = 0
            for n in res[-1]:
                curr_sum += (int(n)**2)
            
            if curr_sum == 1:
                return True
            
            if str(curr_sum) in res:
                return False

            res.append(str(curr_sum))