class Solution(object):

    def maxValueAfterReverse(self, A):
        n = len(A)
        total = res = sum(abs(a - b) for a, b in zip(A, A[1:]))
        max2, min2 = sorted(A[:2])
        # print total
        for a, b in zip(A, A[1:]):
            # print 'meet', a, b
            # print "min2", min2, "max2", max2
            # print total - abs(a - b) + abs(A[0] - b)
            res = max(res, total - abs(a - b) + abs(A[0] - b))
            # print total - abs(a - b) + abs(A[-1] - a)
            res = max(res, total - abs(a - b) + abs(A[-1] - a))
            # print total + (min(a, b) - min2) * 2
            res = max(res, total + (min(a, b) - min2) * 2)
            # print total + (max2 - max(a, b)) * 2
            res = max(res, total + (max2 - max(a, b)) * 2)

            min2 = min(min2, max(a, b))
            max2 = max(max2, min(a, b))
        return res
