# Theory
'''

Prim's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a weighted undirected graph. 
A minimum spanning tree is a tree that connects all nodes in a graph with the minimum total edge weight.

Here are the steps to execute Prim's algorithm:

Choose any vertex to start with and add it to the MST.
1)Find the edge with the smallest weight that connects any vertex in the MST to a vertex not in the MST.
2)Add the new vertex and edge to the MST.
3)Repeat steps 2 and 3 until all vertices are in the MST.
'''

def prim(graph):
    mst = []
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]

    while edges:
        cost, frm, to = min(edges)
        edges.remove((cost, frm, to))
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost_next in graph[to].items():
                if to_next not in visited:
                    edges.append((cost_next, to, to_next))

    return mst
graph = {'A': {'B': 2, 'C': 3}, 'B': {'A': 2, 'C': 4}, 'C': {'A': 3, 'B': 4}}
print(prim(graph))
