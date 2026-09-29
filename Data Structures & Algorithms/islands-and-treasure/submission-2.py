from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        deq = deque() 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    deq.append((r,c))
        
        while deq:
            r,c = deq.popleft()
            for dr,dc in([(0,1), (0,-1), (1,0), (-1,0)]):
                
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0:
                    continue
                if nr >= ROWS or nc >= COLS:
                    continue 
                if grid[nr][nc] == -1:
                    continue 
                if grid[nr][nc] != INF:
                    continue  
                grid[nr][nc] = grid[r][c] + 1
                deq.append((nr,nc))
            

                
                
