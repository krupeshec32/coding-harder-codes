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
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    print('start')
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        #print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                print('value of neighbour:'+str(neighbour))
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
bfs(visited, graph, 'A')
