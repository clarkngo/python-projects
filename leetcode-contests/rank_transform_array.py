class Solution(object):
    def arrayRankTransform(self, A):
        rank = {}
        for i,a in enumerate(sorted(A)):
            if a not in rank:
                rank[a] = len(rank) + 1
        return [rank[a] for a in A]

class Solution(object):
    def arrayRankTransform(self, A):
        vals = sorted(set(A))
        m = {}
        for i, v in enumerate(vals):
            m[v] = i + 1
        return [m[x] for x in A]
