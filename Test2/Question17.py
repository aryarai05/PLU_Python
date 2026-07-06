'''
.Create an undirected graph with the following edges:
* A – B
* A – C
* B – D
* C – D
Display the adjacency list of the graph.
'''
def create_graph():
    graph = {}
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'D']
    graph['D'] = ['B', 'C']
    return graph

def display(graph):
    for i in graph:
        print(i, ":", graph[i])

g = create_graph()
display(g)