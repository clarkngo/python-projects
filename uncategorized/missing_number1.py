# Missing Number
# https://leetcode.com/problems/missing-number/submissions/
# Time Limit Exceed for this solution

def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
def missingNumber(nums):
    bubbleSort(nums)
    n = len(nums)
    if (n == 1):
        if (nums[0] == 0):
            return 1
        else:
            return 0            
    print(hasZero(nums))
    if (hasZero(nums) == False):
            return 0    
    for i in range(n-1):
        print(nums[i+1] - nums[i])
        if (nums[i+1] - nums[i] == 2):
            return nums[i+1] - 1
    print(nums[n-1] + 1)
    return nums[n-1] + 1
    
def hasZero(arr):
    n = len(arr)
    for i in range(n):    
        if arr[i] == 0:
            return True
    return False    
            
nums = [1,2]            
print(missingNumber(nums))