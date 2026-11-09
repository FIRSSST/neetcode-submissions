class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,1,2,3 target = 3
        # 4,5,6,7,1,2,3 target = 5
        # 0,1,2,3,4,5,6 target = 4


        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # [7,8,3,4,5,6]
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        pivot = left # index where pivot is

        if pivot == 0:
            left = 0
            right = len(nums) - 1
         # [7,8,3,4,5,6] target = 4
        # left half:
        if pivot > 0 and target >= nums[0] and target <= nums[pivot - 1]: # it is in the left half
            left = 0
            right = pivot
        else:
            left = pivot
            right = len(nums) - 1
        

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1


