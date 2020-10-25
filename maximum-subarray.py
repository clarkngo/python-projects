class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find largest sum in a contiguous subarray
        O(n) Time 
        """
        cur_sum, max_sum = 0, -sys.maxsize
        for i in range(len(nums)):
            # grow the window if increases current sum
            cur_sum += nums[i]
            # shrink the window to size 1 if current element is larger
            cur_sum = max(nums[i], cur_sum) 
            
            max_sum = max(cur_sum, max_sum)
        return max_sum
        