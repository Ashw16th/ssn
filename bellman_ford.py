def bellman_ford(vertices, edges, source):
    INF = float('inf')
    dist = [INF] * vertices
    dist[source] = 0

    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    for u, v, weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            print("Graph contains a negative weight cycle")
            return None

    return dist

vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []
for _ in range(edges_count):
    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
    edges.append((u - 1, v - 1, weight)) 

source = int(input("Enter source vertex: ")) - 1  

distances = bellman_ford(vertices, edges, source)

if distances:
    print("Shortest distances from source:")
    for i, d in enumerate(distances):
        print(f"Vertex {i+1}: {d if d != float('inf') else 'Unreachable'}")
