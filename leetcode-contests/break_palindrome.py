class Solution(object):
    def breakPalindrome(self, s):
        n = len(s)
        A = list(s)
        if n == 1: return ""

        for i in range(n):
            if A[i] != 'a':
                old = A[i]
                A[i] = 'a'
                if A != A[::-1]:
                    return "".join(A)
                A[i] = old

            if A[i] != 'b' and A[i] > 'b':
                old = A[i]
                A[i] = 'b'
                if A != A[::-1]:
                    return "".join(A)
                A[i] = old

        ans = "".join(A) if A != A[::-1] else None
        for i in range(n-1, -1,-1):
            if A[i] != 'b':
                old = A[i]
                A[i] = 'b'
                if A != A[::-1]:
                    cand = "".join(A)
                    if ans is None:
                        ans = cand
                    elif cand < ans:
                        ans = cand

                A[i] = old

        return ans if ans is not None else ""
