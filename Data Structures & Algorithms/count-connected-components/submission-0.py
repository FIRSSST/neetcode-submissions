class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        connected_components = 0 
        adjLst = { i: [] for i in range (n)}

        for edge1, edge2 in edges:
            adjLst[edge1].append(edge2)
            adjLst[edge2].append(edge1)
        

       
        visited = n * [False]
        
        def dfs(node,visited):
            stack = [node]
            while stack:
                node = stack.pop() 
                if visited[node] == False:
                    visited[node] = True
                    for neighbor in adjLst[node]:
                        stack.append(neighbor)

        for node in range (n):
            if visited[node] == False:
                connected_components += 1
                dfs(node, visited)
        return connected_components


