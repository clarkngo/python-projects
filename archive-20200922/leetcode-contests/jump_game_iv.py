"""
Jump Game IV

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.



Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3


Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
"""

# Consider it is a graph. So we just want to get the longest path in the graph.

# The neighbors can get from an extendtion from i to j by contistanly +1 or -1 until i +d and i - d, all the arr[j] < arr[i] before we meet first arr[j] >= arr[i] will be the neighbors. once we meet the a arr[j] >= arr[i] the following cannot be the neighbors.

# Other's solution
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = dict()
        def dfs(i,arr):
            if i in dp: return dp[i]
            pathlen = 0
            for j in range(i + 1, i + d + 1):
                if len(arr) <= j or arr[j] >= arr[i]: break
                pathlen = max(dfs(j,arr), pathlen)
            for j in range(i-1, i-d-1,-1):
                if j < 0 or arr[j] >= arr [i]: break
                pathlen = max(dfs(j,arr), pathlen)
            dp[i] = pathlen + 1
            return dp[i]
        longestpath = 0
        for i in range(len(arr)):
            longestpath = max(dfs(i,arr),longestpath)
        return longestpath
