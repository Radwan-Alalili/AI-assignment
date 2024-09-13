
def dfs(graph, node, destination, path=None, visited=None):
    
    if path is None:
        path = []
    
    if visited is None:
        visited = set()

    path.append(node)
    visited.add(node)

    if node == destination:
        print("Path:", " : ".join(path))
    
    else:
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, destination, path, visited)
    

    path.pop()
    visited.remove(node)
    

graph = {
    'ONE': ['TWO', 'THREE','FOUR' ],
    'TWO': ['FOUR', 'FIVE', 'FIVE'],
    'THREE': ['FOUR','SIX'],
    'FOUR': ['SEVEN','FIVE'],
    'FIVE': ['SIX'],
    'SIX': ['SEVEN'],
    'SEVEN': []
     }

root = 'ONE'
destination = 'SEVEN'
dfs(graph, root, destination)

print(" ")
print(" function finash successfully")
print(" thank you for tring")
