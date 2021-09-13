graph = {
    'A': ['B', 'C'],
    'B': ['E'],
    'E': ['F', 'G'],
    'F': [],
    'G': [],
    'C': ['H', 'I'],
    'H': [],
    'I': []
}

visited = []  # List to keep track of visited nodes.


def dfs(visited, node):
    visited.append(node)
    print(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(visited, neighbour)


# Driver Code
dfs(visited, 'A')
