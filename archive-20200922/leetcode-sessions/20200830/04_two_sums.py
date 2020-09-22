class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_d = {}
        for i in range(len(nums)):
            if nums[i] not in num_d:
                num_d[nums[i]] = i
            diff = target - nums[i]
            if diff in num_d and num_d[diff] != i:
                return [i, num_d[diff]]
