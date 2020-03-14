# Coding Interview Prep

https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU?fbclid=IwAR1i0M8Xilh-mz86SdDd4zFSNk4uZkuCAwDNUSzLvnOAaM-GPi129FN97q8

## Array

### Two Sum - https://leetcode.com/problems/two-sum/
- initialize a dictionary
- loop over the list
  - calculate the difference of the target and current number
  - if difference NOT in the dictionary
    - add to dictionary with current number as key and current index as value
  - else
    - return list with current index and the value of the difference in the dictionary

### Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- initialize `max_profit` and `profit` to `0` and `min_price` to `float('inf)`
- iterate over the list
  - reassign the value of `min_price` with minimum between `min_price` and the current `price`
  - reassign the value of `profit` with current `price` minus `min_price`
  - reassign the value of `max_profit` with maximum between `max_profit` and current `profit`
- return `max_profit`

### Contains Duplicate - https://leetcode.com/problems/contains-duplicate/
- create a `set` with the given `list`
- check the length of given `list` and compare it with the created `set`
- if both lengths are the same, return `True`
- else, return `False`

### Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/
- initialize `product` to `1`, `n` to length of given list, `output` to an empty list
- iterate over the list
  - append the the current `product` to the `output` list
  - reassign the value of `product` with `product` multiplied by the current number
- reinitialize `product` to `1`
- iterate over the list backward `(n-1, -1, -1)`
  - reassign the value of an element in the list `output[i]` with `output[i]` multiplied by the current `product`
  - reassign the value of `product` with `product` multipled by the current number
- return the `output` list

### Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
- edge case: if length is 1, return the first element
- initialize both `current_sum` and `maximum_sum` with the first element
- iterate over the list starting from index 1
  - accumulate `current_sum` with current number
  - reassign `current_sum` with the maximum between `current_sum` and current number
  - reassign `maximum_sum` with the maximum between `maximum_sum` and `current_sum`
- return `maximum_sum`

### Maximum Product Subarray - https://leetcode.com/problems/maximum-product-subarray/
- initialize a new list `B` with the reverse of the given list `A` `[::-1]`
- iterate over the given list skipping the first index
  - reassign the value of `A[i]` with multiplying `A[i]` and `A[i-1] or 1` (if `A[i-1]` is `0`, `1` will be used instead)
  - reassign the value of `B[i]` with multiplying `B[i]` and `B[i-1] or ` (if `B[i-1]` is `0`, `1` will be used instead)
- return the largest product with `max` in both lists `max(A+B)`

### Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- binary search
- initialize `left` with `0` and `right` with `length - 1`
- create a while loop with condition `left < right`
  - reassign value of `mid` with `(left + right) // 2`
  - if middle number `nums[mid]` is greater than rightmost number `nums[right]`
    - reassign value of `left` with `mid + 1`
  - else
    - reassign value of `right` with `mid`
- return leftmost value `nums[left]` (note: you can also use `nums[right]` or `nums[mid]` as they would have the same index at this line)

### Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/
- binary search
- initialize `left` with `0` and `right` with `length`
- create a while loop with condition `left < right`
  - reassign value of `mid` with `(left + right) // 2`
  - if `target` is less than `nums[0]`, and `nums[0]` is less than `nums[mid]`
    - reassign value of `left` with `mid + 1`
  - else if `target` is greater than `nums[0]`, and `nums[0]` is greater than `nums[mid]`
    - reassign value of `right` with `mid`
  - else if `nums[mid]` is less than `target`
    - reassign value of `left` with `mid + 1`
  - else if `nums[mid]` is greater than `target`
    - reassign value of `right` with `mid`
  - else
    - return `mid`
- return `-1`

### 3Sum - https://leetcode.com/problems/3sum/
### Container With Most Water - https://leetcode.com/problems/container-with-most-water/

---

## Binary

### Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/
### Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/
### Counting Bits - https://leetcode.com/problems/counting-bits/
### Missing Number - https://leetcode.com/problems/missing-number/
### Reverse Bits - https://leetcode.com/problems/reverse-bits/

---

## Dynamic Programming

### Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
### Coin Change - https://leetcode.com/problems/coin-change/
### Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/
### Longest Common Subsequence -
### Word Break Problem - https://leetcode.com/problems/word-break/
### Combination Sum - https://leetcode.com/problems/combination-sum-iv/
### House Robber - https://leetcode.com/problems/house-robber/
### House Robber II - https://leetcode.com/problems/house-robber-ii/
### Decode Ways - https://leetcode.com/problems/decode-ways/
### Unique Paths - https://leetcode.com/problems/unique-paths/
### Jump Game - https://leetcode.com/problems/jump-game/

---

## Graph

### Clone Graph - https://leetcode.com/problems/clone-graph/
### Course Schedule - https://leetcode.com/problems/course-schedule/
### Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow/
### Number of Islands - https://leetcode.com/problems/number-of-islands/
### Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/
### Alien Dictionary (Leetcode Premium) - https://leetcode.com/problems/alien-dictionary/
### Graph Valid Tree (Leetcode Premium) - https://leetcode.com/problems/graph-valid-tree/
### Number of Connected Components in an Undirected Graph (Leetcode Premium) - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

---

## Interval

### Insert Interval - https://leetcode.com/problems/insert-interval/
### Merge Intervals - https://leetcode.com/problems/merge-intervals/
### Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/
### Meeting Rooms (Leetcode Premium) - https://leetcode.com/problems/meeting-rooms/
### Meeting Rooms II (Leetcode Premium) - https://leetcode.com/problems/meeting-rooms-ii/

---

## Linked List

### Reverse a Linked List - https://leetcode.com/problems/reverse-linked-list/
### Detect Cycle in a Linked List - https://leetcode.com/problems/linked-list-cycle/
### Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/
### Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
### Remove Nth Node From End Of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
### Reorder List - https://leetcode.com/problems/reorder-list/

---

## Matrix

### Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/
### Spiral Matrix - https://leetcode.com/problems/spiral-matrix/
### Rotate Image - https://leetcode.com/problems/rotate-image/
### Word Search - https://leetcode.com/problems/word-search/

---

## String

### Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
### Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/
### Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
### Valid Anagram - https://leetcode.com/problems/valid-anagram/
### Group Anagrams - https://leetcode.com/problems/group-anagrams/
### Valid Parentheses - https://leetcode.com/problems/valid-parentheses/
### Valid Palindrome - https://leetcode.com/problems/valid-palindrome/
### Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
### Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/
### Encode and Decode Strings (Leetcode Premium) - https://leetcode.com/problems/encode-and-decode-strings/

---

## Tree

### Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/
### Same Tree - https://leetcode.com/problems/same-tree/
### Invert/Flip Binary Tree - https://leetcode.com/problems/invert-binary-tree/
### Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/
### Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/
### Serialize and Deserialize Binary Tree - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
### Subtree of Another Tree - https://leetcode.com/problems/subtree-of-another-tree/
### Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
### Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/
### Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
### Lowest Common Ancestor of BST - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
### Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/
### Add and Search Word - https://leetcode.com/problems/add-and-search-word-data-structure-design/
### Word Search II - https://leetcode.com/problems/word-search-ii/

---

## Heap

### Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
### Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
### Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

