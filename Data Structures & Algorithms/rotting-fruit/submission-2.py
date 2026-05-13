class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        deq = deque() 
        fresh = 0 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    deq.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

      
        time = 0 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while deq:
            size = len(deq)
            rotten_this_level = False
            for _ in range(size):
                row, col = deq.popleft() 
                for x,y in directions:
                    new_row = row + x
                    new_col = col + y
                    if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                        if grid[new_row][new_col] == 1:
                            fresh -= 1
                            grid[new_row][new_col] = 2
                            rotten_this_level = True
                            deq.append((new_row, new_col))

            if rotten_this_level == True:
                time += 1

        if fresh > 0 :
            return -1



        return time 