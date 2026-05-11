class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjLst = {i: [] for i in range(n)}

        if len(edges) != n - 1:
            return False

        for edge1, edge2 in edges:
            if edge1 in adjLst:
                adjLst[edge1].append(edge2)
            else:
                adjLst[edge1] = []
                adjLst[edge1] = [edge2]
            
            if edge2 in adjLst:
                adjLst[edge2].append(edge1)
            else:
                adjLst[edge2] = []
                adjLst[edge2] = [edge1]
        
        visited = n * [False]
        node = 0
        stack = [(node, -1)] # current_node, parent_node
        print(adjLst)
        #print(stack)
        while stack:
            node, parent = stack.pop() 
            if visited[node] == True:
                return False
            visited[node] = True
            print("Visited", node)
            for neighbor in adjLst[node]:
                if neighbor == parent:
                    continue
                stack.append((neighbor, node))
        
        
    
        
        return all(visited)

            