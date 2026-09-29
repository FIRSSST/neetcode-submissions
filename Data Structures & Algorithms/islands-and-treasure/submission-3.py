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
                #Choice A: Direct Parent Offset (No Layer Loop)
                #You assign distance to neighbors when you discover them:
                grid[nr][nc] = grid[r][c] + 1
                deq.append((nr,nc))

            #Choice B: Level-by-Level Loop (Layer Wave)
            #If you want to use a global dist counter, you must group pops using for _ in range(len(deq)) so every node in the same layer shares the same dist:
            """
            dist = 0
            while deq:
                # Process every node at the CURRENT distance level together
                for _ in range(len(deq)): # process ENTIRE layer
                    r, c = deq.popleft()
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                            grid[nr][nc] = dist + 1  # Or assign at the layer level
                            deq.append((nr, nc))
                            
                dist += 1  # Increment ONLY after processing an entire layer


            """
            

                
                
