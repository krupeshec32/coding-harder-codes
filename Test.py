import sys

a = [1, 0, 7, 15, 10]
temp = a[0]


def getMax(a,temp):
    for i in a:
        if temp > i:
            temp = temp
        else:
            temp = i
    print(temp)


def getMin(a,temp):
    for i in a:
        if temp < i:
            temp = temp
        else:
            temp = i
    print(temp)

def graphDFS(graph, node,visited):
    visited.append(node)
    print(node)
    for neighbor in graph[node]:
        graphDFS(graph,neighbor,visited)

def graphBFS(graph,node,visited,queue):
    visited.append(node)
    queue.append(node)

    while queue:
        s=queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



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
visited=[]
queue=[]

#graphDFS(graph,'A',visited)
graphBFS(graph,'A',visited,queue)


#getMax(a,temp)
#print("*******")
#getMin(a,temp)
#if(1==1 and 2==2):
#    print('hi')