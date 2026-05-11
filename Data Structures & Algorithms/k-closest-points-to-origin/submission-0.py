import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        distances = {}
        for point in points:
            x1,y1 = point[0], point[1]
            x2,y2 = 0,0

            dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

            if dis in distances:
                distances[dis].append(point)
            else:
                distances[dis] = [point]

            heapq.heappush(minHeap, dis)
        
        lst = []
        for i in range (0, k):
            dis = heapq.heappop(minHeap)
            if dis in distances:
                lst.append(distances[dis].pop())
        
        return lst
