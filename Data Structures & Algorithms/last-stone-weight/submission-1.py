import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -1 * stone)
        #print(maxHeap)
        while len(maxHeap) > 1:
            first_largest = heapq.heappop(maxHeap) * -1
            second_largest = heapq.heappop(maxHeap) * -1

           # print('first:', first_largest)
           # print('second:', second_largest)
            #if first_largest == second_largest:
                # don't add them back
            if first_largest != second_largest:
                new_stone = abs(second_largest - first_largest) 
            #    print("readding: ", new_stone)
                heapq.heappush(maxHeap, new_stone * -1)
            #    print(maxHeap)
        
        if not maxHeap:
            return 0

        return maxHeap[0] * -1