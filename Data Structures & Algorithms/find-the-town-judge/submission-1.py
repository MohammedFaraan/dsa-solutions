class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        nums = defaultdict(list)

        for p, t in trust:
            if p not in nums:
                nums[p].extend([0, 0])           
            nums[p][0] += 1

            if t not in nums: 
                nums[t].extend([0, 0])
            nums[t][1] += 1 
        
        
        for p, [trusts, trustees] in nums.items():
            if trusts == 0 and trustees == len(nums) -1:
                return p
                
        return -1