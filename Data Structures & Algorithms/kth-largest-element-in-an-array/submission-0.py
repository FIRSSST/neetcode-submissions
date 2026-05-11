import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:

            heapq.heappush(maxHeap, num * -1)
         
        lst = []

        if k == 1:
            return maxHeap[0] * -1
        for i in range (k-1):
            heapq.heappop(maxHeap)
            

        return maxHeap[0] * -1