
def dijkstra(graph, start):
    # Create a dictionary to store the distance from the start vertex to each vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Create a dictionary to store the previous vertex in the shortest path
    previous = {vertex: None for vertex in graph}

    # Create a set to store the vertices that have already been visited
    visited = set()

    # Loop over all vertices in the graph
    while len(visited) < len(graph):
        # Get the unvisited vertex with the smallest distance from the start vertex
        current_vertex = None
        current_distance = float('inf')
        for vertex in graph:
            if vertex not in visited and distances[vertex] < current_distance:
                current_vertex = vertex
                current_distance = distances[vertex]

        # If there are no unvisited vertices left, we're done
        if current_vertex is None:
            break

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # Loop over the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate the distance to the neighbor through the current vertex
            distance = current_distance + weight

            # If the new distance is shorter than the distance in the distances dictionary, update the distances dictionary and the previous dictionary
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex

    return distances, previous

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {'E': 1},
    'E': {}
}

start = 'A'
print(dijkstra(graph, start))