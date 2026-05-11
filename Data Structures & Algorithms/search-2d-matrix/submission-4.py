class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0 
        right = len(matrix) * len(matrix[0]) - 1
        n = len(matrix[0])
        while left <= right:
            mid = int ( left + ((right - left) / 2) ) 

            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
        return False