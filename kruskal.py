class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u - 1, v - 1))  # Convert 1-based to 0-based indexing

    def find_mst(self):
        self.edges.sort()
        ds = DisjointSet(self.vertices)
        mst = []
        mst_cost = 0

        for weight, u, v in self.edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u + 1, v + 1, weight))  # Convert back to 1-based for output
                mst_cost += weight

        return mst, mst_cost

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

kruskal = Kruskal(vertices)

for _ in range(edges):
    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
    kruskal.add_edge(u, v, weight)

mst, cost = kruskal.find_mst()

print("\nMinimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")

print("Total MST Cost:", cost)
