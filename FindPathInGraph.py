class FindPathInGraph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.queue = []

    def printPathDFS(self, graph, start, end):
        if start not in self.visited:
            self.visited.append(start)
        for neighbour in graph[start]:
            if neighbour not in self.visited:
                self.visited.append(neighbour)
                if neighbour == end:
                    print(self.visited)
                self.printPathDFS(graph, neighbour, end)

    def printPathBFS(self, graph, start, end):
        self.visited.append(start)
        self.queue.append(start)

        while self.queue:
            s = self.queue.pop(0)
            for neighbour in graph[s]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)
                    if neighbour == end:
                        print(self.visited)


graph = {'A': ['B', 'E', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

x = FindPathInGraph(graph)
# x.printPathDFS(graph, 'A', 'D')
x.printPathBFS(graph, 'A', 'D')
