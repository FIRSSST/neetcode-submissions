class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        TOP = 0
        BOTTOM = len(matrix) - 1
        LEFT = 0 
        RIGHT = len(matrix[0]) - 1

        res = []
        while TOP <= BOTTOM and LEFT <= RIGHT:
           
            for i in range(LEFT, RIGHT + 1):
                res.append(matrix[TOP][i]) 
            TOP += 1
            
            for i in range(TOP, BOTTOM + 1):
                res.append(matrix[i][RIGHT])
            RIGHT -= 1

            if TOP <= BOTTOM:
                for i in range(RIGHT, LEFT - 1, -1):
                    res.append(matrix[BOTTOM][i])
                BOTTOM -= 1
            if LEFT <= RIGHT:
                for i in range(BOTTOM, TOP - 1, -1):
                    res.append(matrix[i][LEFT]) 
                LEFT += 1
        
        return res