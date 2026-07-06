#Perform a Breadth-First Search (BFS) traversal starting from vertex A.
def create_graph():
    graph = {}
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'D']
    graph['D'] = ['B', 'C']
    return graph

def bfs(graph, start):
    queue = [start]
    result = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in result:
            result.append(vertex)
            print(vertex, end=" ")
            for i in graph[vertex]:
                if i not in result:
                    queue.append(i)

g = create_graph()
bfs(g, 'A')