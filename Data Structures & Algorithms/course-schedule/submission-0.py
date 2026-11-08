from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjLst = defaultdict(list)

        for a,b in prerequisites:
            adjLst[a].append(b)

        UNSEEN = 0
        VISITING = 1
        VISITED = 2

        seen = [UNSEEN] * numCourses

        def dfs(node):
            if seen[node] == VISITED:
                return True
            if seen[node] == VISITING:
                return False
            
            seen[node] = VISITING

            for neighbor in adjLst[node]:
                if dfs(neighbor) != True:
                    return False 
            
            seen[node] = VISITED
            return True

        

        for node in range(numCourses): #for node in adjLst: cant do this it misses courses that do not have prereqs
            if dfs(node) != True:
                return False
            
        return True