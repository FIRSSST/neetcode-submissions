class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # check columns:
        top = 0 
        bottom = len(matrix) - 1
        # target = 4
        while top <= bottom:
            mid = int ( top + (bottom - top)/2 )
            print("MID:", matrix[mid][0], "TOP:", top, "BOTTOM:", bottom)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        
        rowToSearch = top - 1
        print(rowToSearch, 'row to search')
        left = 0
        right = len(matrix[rowToSearch]) - 1
        while left <= right:
            mid = int(left + (right - left)/2)

            if matrix[rowToSearch][mid] == target:
                return True
            elif matrix[rowToSearch][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False