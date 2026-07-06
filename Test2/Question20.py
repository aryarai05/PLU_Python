#Perform a Depth-First Search (DFS) traversal starting from vertex A.
def create_graph():
    graph = {}
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'D']
    graph['D'] = ['B', 'C']
    return graph

def dfs(graph, start, result=[]):
    if start not in result:
        result.append(start)
        print(start, end=" ")
        for i in graph[start]:
            dfs(graph, i, result)

g = create_graph()
dfs(g, 'A')