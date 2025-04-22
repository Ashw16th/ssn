def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = [source]
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    max_flow = 0
    parent = [-1] * len(graph)

    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        max_flow += path_flow

    print("\nMaximum Flow:", max_flow)

n = int(input("Enter the number of vertices: "))

print("\nEnter the capacity matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]

source, sink = map(int, input("\nEnter source and sink: ").split())

ford_fulkerson(graph, source, sink)
