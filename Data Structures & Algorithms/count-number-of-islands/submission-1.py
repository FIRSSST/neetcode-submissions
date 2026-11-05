class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        visited = set() 
        number_of_islands = 0


        def dfs(r,c):
            if r >= rows or r < 0:
                return
            if c >= cols or c < 0:
                return
            if (r,c) in visited:
                return
            if grid[r][c] == "0":
                return

            visited.add((r,c))

            for dr,dc in ([(0,1), (0,-1), (1,0), (-1, 0)]):
                nr,nc = r+dr, c+dc
              
                dfs(nr,nc)


        for r in range(rows):
            for c in range(cols):
                if not (r,c) in visited and grid[r][c] == "1":
                    dfs(r,c)
                    number_of_islands += 1
        
        return number_of_islands
