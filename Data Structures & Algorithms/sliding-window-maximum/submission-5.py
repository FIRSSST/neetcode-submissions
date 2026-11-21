import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        res = []
        hp = []
        heapq.heapify(hp)
        for right, num in enumerate(nums):
            heapq.heappush(hp, (num * -1, right))

            if right - left + 1 == k:
                #print(nums[left:right+1])
                #print("HEAP:", hp)
                largest, index = heapq.heappop(hp)
                while index < left and heapq:
                    largest, index = heapq.heappop(hp)
                res.append(-1 * largest)
                if index > left and index <= right:
                    heapq.heappush(hp, (largest, index))
                left += 1
                #print("RES:", res)

        
        return res
