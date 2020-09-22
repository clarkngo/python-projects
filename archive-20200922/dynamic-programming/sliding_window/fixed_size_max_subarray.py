# Resource: https://www.youtube.com/watch?v=MK-NZ4hN7rs
# Find the max sum subarray of a fixed size K
# Example input: [4, 2, 1, 7, 8 ,1, 2, 8, 0]

from typing import List
import sys
INT_MIN = -sys.maxsize -1

def find_max_sum_subarray(arr: List, k: int) -> List:
    max_value: int = INT_MIN
    current_running_sum = 0
    for i in range(len(arr)):
        # adds all the values. i < values < k - 1
        # the first few loops until k - 1 would create the current running sum
        # for the first subarray
        # succeding loops would generate other current running sum for the
        # following subarray
        current_running_sum += arr[i]     # 4, 6, 7, 10, 16, 16, 11, 11, 10
        if i >= k-1:
          max_value = max(max_value, current_running_sum)
          current_running_sum -= arr[i-(k-1)]   # substract the furthest left value of subarray
    return max_value

result = find_max_sum_subarray([4, 2, 1, 7, 8 ,1, 2, 8, 0], 3)
print(result)
