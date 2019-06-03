def merge(arr1, arr2):
  length_difference = len(arr1) - len(arr2)
  j = 0

  # merge two arrays
  for i in range(length_difference, len(arr1)):  
    arr1[i] = arr2[j]
    j += 1

  return bubble_sort(arr1)

## bubble sort
def bubble_sort(arr):

  n = len(arr) 

  # Traverse through all array elements 
  for i in range(n): 

    # Last i elements are already in place 
    for j in range(0, n-i-1): 

    # traverse the array from 0 to n-i-1 
    # Swap if the element found is greater 
    # than the next element 
      if arr[j] > arr[j+1] : 
        arr[j], arr[j+1] = arr[j+1], arr[j] 
  return arr

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]  
merge(nums1, nums2)

### My Leetcode Solution ###
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         length_difference = len(nums1) - len(nums2)
#         k = 0

#         # merge two arrays
#         for l in range(length_difference, len(nums1)):  
#             nums1[l] = nums2[k]
#             k += 1

#                     ## bubble sort
       
#         n = len(nums1) 

#         # Traverse through all array elements 
#         for i in range(n): 
            

#             # Last i elements are already in place 
#             for j in range(0, n-i-1): 

#                 # traverse the array from 0 to n-i-1 
#                 # Swap if the element found is greater 
#                 # than the next element 
#                 if nums1[j] > nums1[j+1] : 
#                     nums1[j], nums1[j+1] = nums1[j+1], nums1[j] 

# Runtime: 56 ms, faster than 10.44% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.3 MB, less than 11.26% of Python3 online submissions for Merge Sorted Array.
