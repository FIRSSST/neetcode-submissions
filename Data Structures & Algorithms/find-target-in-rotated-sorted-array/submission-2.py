class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,1,2,3 target = 3
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 

        min_index = left 
        #print('min_index is ', left, nums[left])
        if min_index > 0 and nums[0] <= target <= nums[min_index - 1]:
            left = 0
            right = min_index
        else:
            left = min_index
            right = len(nums) - 1
        #print("Left indx is ", left, "Right indx is", right, 'Searching from ', nums[left], 'to',nums[right])
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1