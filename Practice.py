class Practice:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.queue=[]

    '''
        visited.append(node)
    print(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(visited, neighbour)

    '''

    def getDFS(self, graph, node):

        if node not in self.visited:
            self.visited.append(node)
            print(node)
            for i in graph[node]:
                if i != []:
                    self.getDFS(graph, i)

    def getBFS(self,graph,node):
        self.visited.append(node)
        self.queue.append(node)

        while self.queue:
            s=self.queue.pop(0)
            print(s)
            for i in graph[s]:
                if i not in self.visited:
                    self.visited.append(i)
                    self.queue.append(i)




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
x = Practice(graph)
#x.getDFS(graph, 'A')
print('*******')
x.getDFS(graph,'A')
