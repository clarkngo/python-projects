class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) == 0 and len(B) == 0:
            return True
        for i in range(len(A)):
            test_str = A[i:] + A[:i]
            if test_str == B:
                return True
        return False