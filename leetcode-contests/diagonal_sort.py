class Solution(object):
    def diagonalSort(self, A):
        R, C = len(A), len(A[0])
        vals = collections.defaultdict(list)
        for r, row in enumerate(A):
            for c,v  in enumerate(row):
                vals[r-c].append(v)
        for row in vals.values():
            row.sort(reverse=True)
        for r, row in enumerate(A):
            for c,v  in enumerate(row):
                A[r][c] = vals[r-c].pop()
        return A
