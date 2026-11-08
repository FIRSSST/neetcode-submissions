class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjLst = defaultdict(list)
        for a,b in prerequisites:
            adjLst[a].append(b)
        
        UNSEEN = 0
        VISITING = 1
        VISITED = 2

        seen = [UNSEEN] * numCourses
        courses = []

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
            courses.append(node)
            return True
        

        for node in range(numCourses):
            if dfs(node) != True:
                return [] 
        
        return courses
        

            