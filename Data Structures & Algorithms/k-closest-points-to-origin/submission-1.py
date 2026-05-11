import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] #O(N)
       
        for point in points: #O(N)
            x1,y1 = point[0], point[1]
            x2,y2 = 0,0

            dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

            
            heapq.heappush(minHeap, (dis, point))
        
        lst = []
        for i in range (0, k): #O(k)
            dis = heapq.heappop(minHeap)[1]
            lst.append(dis)
              
        
        return lst

        #Runtime Complexity: O(N) * O(log(N)) + O(k)
        #Spacetime: O(N)
