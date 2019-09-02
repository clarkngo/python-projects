# Source: https://leetcode.com/problems/duplicate-zeros/

# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything
# from your function.

# Example 1:

# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Runtime: 88 ms, faster than 31.69% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        print(arr)
        hasZero = False
        count = 0
        for i in range(len(arr)):
          if hasZero == True:
            hasZero = False
            continue
          if arr[i] == 0:
            arr.insert(i+1, 0)
            hasZero = True
            count += 1
        while count != 0:
          arr.pop()
          count -= 1
        print(arr)

a = Solution()
a.duplicateZeros([1,0,2,3,0,4,5,0])
