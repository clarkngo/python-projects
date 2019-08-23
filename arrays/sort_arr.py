class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squared = []
        for num in A:
            squared.append(num**2)
        squared.sort()
        return squared
