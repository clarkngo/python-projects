# Resource: https://www.youtube.com/watch?v=MK-NZ4hN7rs
# Smallest Subarray with Given Sum

from typing import List
import sys
INT_MAX = sys.maxsize
def smallest_subarray(target_sum: int, arr: List) -> int:
    min_window_size = INT_MAX
    current_window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        current_window_sum += arr[window_end]

        while current_window_sum >= target_sum:
            min_window_size = min(current_window_sum, window_end - window_start + 1)
            current_window_sum -= arr[window_start]   # shrink with the leftmost value
            window_start += 1                         # increment the left pointer
    return min_window_size

arr = [4,2,2,7,8,1,2,8,10]
target_sum = 8
result = smallest_subarray(target_sum, arr)
print(result)
