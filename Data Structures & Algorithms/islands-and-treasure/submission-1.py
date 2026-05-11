from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
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
            if (row,col) in visited:
                continue
            
            if grid[row][col] >= distance:
                grid[row][col] = distance 
            
            visited.add((row,col))
            
            deq.append((row+1, col, distance+1))
            deq.append((row-1, col, distance+1))
            deq.append((row, col+1, distance+1))
            deq.append((row, col-1, distance+1))


        