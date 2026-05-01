class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums )
        res=[1]*(n)

        for i in range(1, n):
            prod=nums[i-1]*res[i-1]
            res[i]=prod
        
        suffix=1
        for i in range(n-2, -1,-1):
            suffix*=nums[i+1]
            res[i]=suffix*res[i]
             
        return res
