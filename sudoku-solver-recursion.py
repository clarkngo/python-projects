class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def possible(y,x,n):
            for i in range(0,9):
                if board[y][i] == n:
                    return False
            for i in range(0,9):
                if board[i][x] == n:
                    return False
            x0 = (x//3) * 3
            y0 = (y//3) * 3
            for i in range(0,3):
                for j in range(0,3):
                    if board[y0+i][x0+i] == n:
                        return False
            return True
        def solve():
            for y in range(9):
                for x in range(9):
                    if board[y][x] == ".":
                        for n in range(1,10):
                            if possible(x,y,n):
                                board[y][x] = n
                                solve()
                                board[y][x] = "."
                        return
        
        
        solve() 
        
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
a = Solution()
a.solveSudoku(board)
print(board)
