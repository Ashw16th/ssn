def is_safe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:  
        return False             #no cycle
    if v in path: 
        return False                #already visited
    return True

def hamiltonian_cycle_util(graph, path, pos, n):
    if pos == n:
        if graph[path[pos - 1]][path[0]] == 1:              #return
            return True
        return False

    for v in range(1, n):           #next V
        if is_safe(v, graph, path, pos):
            path[pos] = v           #place V
            if hamiltonian_cycle_util(graph, path, pos + 1, n):  
                return True             
            path[pos] = -1     #backtrack

    return False

def hamiltonian_cycle(graph):           #main
    n = len(graph)
    path = [-1] * n
    path[0] = 0

    if not hamiltonian_cycle_util(graph, path, 1, n):
        print("No Hamiltonian Cycle exists")
    else:
        print("Hamiltonian Cycle found:", path + [path[0]])

n = int(input("Enter number of vertices: "))
graph = []
print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

hamiltonian_cycle(graph)
