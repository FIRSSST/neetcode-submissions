class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [ [False] * cols for i in range(rows) ]
        components = 0 

        def dfs(row, col):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return 
            if grid[row][col] != '1':
                return
            if visited[row][col] == True:
                return 
            
            visited[row][col] = True 

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and visited[row][col] is False:
                    components += 1
                    dfs(row, col)
        
        return components