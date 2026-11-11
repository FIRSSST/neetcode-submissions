class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and seen[nums[i]] >= 1:
                return nums[i]
            else:
                seen[nums[i]] = 1
        
        