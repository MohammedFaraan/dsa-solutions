class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0
        
        # Base case: A prefix sum of 0 has occurred 1 time
        # This handles the case when a subarray starting from index 0 equals k
        prefix_counts = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - k) exists, add its frequency to our result
            if (current_sum - k) in prefix_counts:
                res += prefix_counts[current_sum - k]
            
            # Record the current prefix sum frequency
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
            
        return res