'''
Kruskal's algorithm is another greedy algorithm used to find the minimum spanning tree (MST) of a weighted undirected graph. Like Prim's algorithm, Kruskal's algorithm also finds the MST by adding edges to a set, but it does so in a different way.

Here are the steps to execute Kruskal's algorithm:

1)Create a set of edges sorted by their weights.
2)Initialize an empty set of edges to represent the MST.
3)For each edge in the set of edges:
    a. If adding the edge to the MST does not create a cycle, add it to the MST.
4)Return the MST.
'''


def kruskal(graph):
    # Create a list of edges sorted by their weights
    edges = [(cost, frm, to) for frm in graph for to, cost in graph[frm].items()]
    edges.sort()

    # Initialize an empty list to store the MST
    mst = []

    # Create a dictionary to keep track of which vertices are in which components
    components = {v: v for v in graph}

    # Loop over the sorted edges
    for cost, frm, to in edges:
        # If the two vertices are not in the same component, add the edge to the MST and merge the components
        if components[frm] != components[to]:
            mst.append((frm, to, cost))
            old_component = components[to]
            new_component = components[frm]
            for v in components:
                if components[v] == old_component:
                    components[v] = new_component

    return mst
graph = {'A': {'B': 2, 'C': 3}, 'B': {'A': 2, 'C': 4}, 'C': {'A': 3, 'B': 4}}
print(kruskal(graph))
