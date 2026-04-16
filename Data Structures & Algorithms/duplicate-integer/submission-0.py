class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        setArr = set()

        for n in nums:
            if n in setArr:
                return True
            else:
                setArr.add(n)

        return False 