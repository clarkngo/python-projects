"""
Time O(n^2)
Space O(1)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i , j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
"""
Time O(n^2)
Space O(n^2)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        print(visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    self.dfs(grid, i , j, visited)
                    count += 1
        return count
    
    def dfs(self, grid, i, j, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1" or visited[i][j] == True:
            return
        visited[i][j] = True
        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i, j+1, visited)
        self.dfs(grid, i, j-1, visited)
        