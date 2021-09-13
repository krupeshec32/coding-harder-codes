from Edge import Edge
from WeightedGraphNode import WeightedGraphNode


class WeightedGraph:
    def __init__(self, edges, N):
        # A list of lists to represent an adjacency list
        # if number of vertices 4, the below line has [None,None,None,None]
        self.adj = [None] * N

        # allocate memory in adj metrix
        for i in range(N):
            self.adj[i] = []

        for e in edges:
            # allocate node in adjacency list from src to dest
            node = WeightedGraphNode(e.dest, e.weight)
            self.adj[e.src].append(node)

    def printGraph(graph):
        for src in range(len(graph.adj)):
            # print current vertex and all its neighboring vertices
            for edge in graph.adj[src]:
                print(f"({src} —> {edge.val}, {edge.weight}) ", end='')
            print()


edges = [Edge(0, 1, 6), Edge(1, 2, 7), Edge(2, 0, 5), Edge(2, 1, 4), Edge(3, 2, 10), Edge(4, 5, 1), Edge(5, 4, 3)]
N = 6
graph = WeightedGraph(edges, N)
graph.printGraph()
