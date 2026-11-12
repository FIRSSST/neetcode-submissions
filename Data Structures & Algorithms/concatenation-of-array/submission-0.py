class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * (2*n)

        for i in range(len(res)):
            indx = i % n
          
            res[i] = nums[indx]
        return res 
        