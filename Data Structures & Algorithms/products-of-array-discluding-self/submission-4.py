class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums )
        prefix=[1]*(n)

        for i in range(1, n):
            prod=nums[i-1]*prefix[i-1]
            prefix[i]=prod
        
        suffix=[1]*n
        for i in range(n-2, -1,-1):
            prod=nums[i+1]*suffix[i+1]
            suffix[i]=prod
        
        res=[1]*n
        for i in range(n):
            res[i]=prefix[i]*suffix[i]
        
        return res
