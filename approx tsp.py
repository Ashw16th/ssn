import sys

def min_key(n, key, mst_set):
    min_value = sys.maxsize
    min_index = -1
    for v in range(n):
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_index = v
    return min_index

def prim_mst(n, graph):
    parent = [-1] * n
    key = [sys.maxsize] * n
    mst_set = [False] * n
    key[0] = 0

    for _ in range(n - 1):
        u = min_key(n, key, mst_set)
        mst_set[u] = True

        for v in range(n):
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent

def preorder_traversal(parent, node, visited, path):
    visited[node] = True
    path.append(node)
    for i in range(len(parent)):
        if parent[i] == node and not visited[i]:
            preorder_traversal(parent, i, visited, path)

def tsp_approx(n, graph):
    parent = prim_mst(n, graph)
    visited = [False] * n
    path = []
    preorder_traversal(parent, 0, visited, path)
    path.append(0)

    cost = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))

    print("\nApproximate Minimum Cost:", cost)
    print("Approximate Tour:", path)

n = int(input("Enter number of cities: "))
graph = [list(map(int, input().split())) for _ in range(n)]

tsp_approx(n, graph)
