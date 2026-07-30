def dfs(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
    }
visited=set()
print('DFS transversal:')
dfs(graph,'A',visited)
      
