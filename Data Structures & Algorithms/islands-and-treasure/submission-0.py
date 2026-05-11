from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [ [False] * cols for _ in range(rows) ]

        deq = deque([])

        # do BFS from gates 

        for row in range (rows):
            for col in range(cols):
                if grid[row][col] == 0: # gate
                    deq.append((row,col,0)) # row, col, distance

        if len(deq) == 0:
            return # no gates
        
        while deq:
            row, col, distance = deq.popleft()
            if row < 0 or row >= rows:
                continue
            if col < 0 or col >= cols:
                continue
            if grid[row][col] == -1:
                continue 
            if visited[row][col] == True:
                continue
            
            if grid[row][col] >= distance:
                grid[row][col] = distance 
            
            visited[row][col] = True
            
            deq.append((row+1, col, distance+1))
            deq.append((row-1, col, distance+1))
            deq.append((row, col+1, distance+1))
            deq.append((row, col-1, distance+1))


        