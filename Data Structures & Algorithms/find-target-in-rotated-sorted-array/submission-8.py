class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,1,2,3 target = 3
        # 4,5,6,7,1,2,3 target = 5
        # 0,1,2,3,4,5,6 target = 4

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        pivot_index = left

        if pivot_index == 0:
            left = 0
            right = len(nums) - 1

        if pivot_index > 0 and target >= nums[0] and target <= nums[pivot_index - 1]: # left side
            left = 0
            right = pivot_index
        else:
            left = pivot_index
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

