class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [ [False] * cols for _ in range(rows) ]

        max_area = 0 

        def dfs(row, col):
            if row < 0 or row >= rows:
                return 0
            if col < 0 or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0
            if visited[row][col] is True:
                return 0

            
            
            visited[row][col] = True
                
            top = dfs(row+1, col)
            bottom = dfs(row-1, col)
            left = dfs(row, col-1)
            right = dfs(row, col+1)

            count = 1 + top + bottom + left + right
            
            return count
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and visited[row][col] is False:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area
            
