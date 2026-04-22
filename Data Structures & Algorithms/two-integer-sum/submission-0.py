class Solution(object):
    def twoSum(self, nums, target):
        hashMap = dict()

        for i in range(len(nums)):
            if target-nums[i] in hashMap:
                return [hashMap[target-nums[i]], i]
            else:
                hashMap[nums[i]] = i
        
        return [-1, -1]
        
        