"""
https://leetcode.com/problems/find-the-town-judge/

Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.



Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

Runtime: 788 ms, faster than 72.99% of Python3 online submissions for Find the Town Judge.
Memory Usage: 17.3 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
"""

# Given = [[1,3],[2,3],[3,1]]
# Expected = -1
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # initialize list of people (as index) with trust value at 0
        # note: we need extra 0 element to match position/index of people
        count = [0] * (N + 1)

        # access nested list with "i, j"
        for i, j in trust:
            # "i" represents a person who trust someone
            # "j" represents a person who was trusted by "i"
            count[i] -= 1   # decrease the trust value
            count[j] += 1   # increase the trust value
        print(count)    # [0, 0, -1, 1]

        # find the town judge (most trusted person)
        for i in range(1, N + 1):

            # N - 1 satisfies:
            #   N = Everybody trusts the town judge
            #   -1 = Except the town judge
            # because of count[i] -= 1:
            #   if the most trusted person trusted someone,
            #   it will not satisfy the condition == N-1
            if count[i] == N - 1:
                return i
        return -1
