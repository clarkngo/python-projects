"""
Maximum Students Taking Exam

Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.



Example 1:


Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.
Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats.

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.


Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8
"""

#
from functools import reduce
class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        def combination_row(i, end=0, prev='', count=0, front=None):
            if end >= n:
                yield prev, count; return
            elif seats[i][end] == '.' and (not prev or prev[-1] == '#') and (end == 0 or front[end-1] == '#') and (end == n-1 or front[end+1] == '#'):
                yield from combination_row(i, end+1, prev+'.', count+1, front)
            yield from combination_row(i, end+1, prev+'#', count, front)

        dp = {'#'*n:0}
        for i in range(m):
            def update(d, k, v):
                d[k] = max(d.get(k, 0), v)
                return d
            dp = reduce(lambda x,pair:update(x,*pair), (k,v+sm) for p,sm in dp.items() for k,v in combination_row(i, front=p)), {})
        return max(dp.values())
