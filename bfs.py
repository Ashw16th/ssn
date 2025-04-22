from collections import deque

class Solution:
    def bfs_of_graph(self, V, adj):
        visited = [False] * V
        queue = deque([0])
        visited[0] = True
        bfs_result = []

        while queue:
            node = queue.popleft()
            bfs_result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return bfs_result

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def print_ans(ans):
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    V = 5
    adj = {i: [] for i in range(V)}
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
    for u, v in edges:
        add_edge(adj, u, v)
    
    obj = Solution()
    bfs_result = obj.bfs_of_graph(V, adj)
    print_ans(bfs_result)



# DFS

class Solution:
    def dfs(self, node, adj, visited, dfs_result):
        visited[node] = True
        dfs_result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited, dfs_result)

    def dfs_of_graph(self, V, adj):
        visited = [False] * V
        dfs_result = []
        self.dfs(0, adj, visited, dfs_result)
        return dfs_result

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def print_ans(ans):
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    V = 5
    adj = {i: [] for i in range(V)}
    edges = [(0, 2), (2, 4), (0, 1), (0, 3)]
    for u, v in edges:
        add_edge(adj, u, v)
    
    obj = Solution()
    dfs_result = obj.dfs_of_graph(V, adj)
    print_ans(dfs_result)


#IDFS

class Solution:
    def idfs_of_graph(self, V, adj):
        visited = [False] * V
        stack = [0]  # Start from node 0
        dfs_result = []

        while stack:
            node = stack.pop()  # Get the last inserted node (LIFO)
            if not visited[node]:
                visited[node] = True
                dfs_result.append(node)
                print(" ".join(map(str, dfs_result)))
                # Push all unvisited neighbors onto the stack
                for neighbor in reversed(adj[node]):  # Reverse for correct order
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return dfs_result

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def print_ans(ans):
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    V = 5
    adj = {i: [] for i in range(V)}
    edges = [(0, 2), (2, 4), (0, 1), (0, 3)]
    for u, v in edges:
        add_edge(adj, u, v)
    
    obj = Solution()
    idfs_result = obj.idfs_of_graph(V, adj)
    print_ans(idfs_result)



    