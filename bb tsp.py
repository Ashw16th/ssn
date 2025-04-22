import sys

class Node:
    def __init__(self, level, path, cost, reduced_matrix):
        self.level = level
        self.path = path
        self.cost = cost
        self.reduced_matrix = reduced_matrix

def reduce_matrix(matrix, n):
    row_min = [min(row) if min(row) != sys.maxsize else 0 for row in matrix]
    for i in range(n):
        if row_min[i] != sys.maxsize:
            for j in range(n):
                if matrix[i][j] != sys.maxsize:
                    matrix[i][j] -= row_min[i]

    col_min = [min(matrix[i][j] for i in range(n)) if min(matrix[i][j] for i in range(n)) != sys.maxsize else 0 for j in range(n)]
    for j in range(n):
        if col_min[j] != sys.maxsize:
            for i in range(n):
                if matrix[i][j] != sys.maxsize:
                    matrix[i][j] -= col_min[j]

    return sum(row_min) + sum(col_min)

def copy_matrix(matrix, n):
    return [[matrix[i][j] for j in range(n)] for i in range(n)]

def tsp_bb(matrix, n):
    min_cost = sys.maxsize
    queue = []
    reduced_matrix = copy_matrix(matrix, n)
    cost = reduce_matrix(reduced_matrix, n)
    queue.append(Node(0, [0], cost, reduced_matrix))

    while queue:
        queue.sort(key=lambda x: x.cost)
        node = queue.pop(0)

        if node.level == n - 1:
            final_cost = node.cost + matrix[node.path[-1]][0]
            if final_cost < min_cost:
                min_cost = final_cost
                best_path = node.path + [0]
            continue

        for i in range(n):
            if i not in node.path:
                new_matrix = copy_matrix(node.reduced_matrix, n)
                for j in range(n):
                    new_matrix[node.path[-1]][j] = sys.maxsize
                    new_matrix[j][i] = sys.maxsize
                new_matrix[i][0] = sys.maxsize
                new_cost = node.cost + matrix[node.path[-1]][i] + reduce_matrix(new_matrix, n)
                queue.append(Node(node.level + 1, node.path + [i], new_cost, new_matrix))

    print("\nMinimum Cost:", min_cost)
    print("Optimal Path:", best_path)

n = int(input("Enter number of cities: "))
matrix = [list(map(int, input().split())) for _ in range(n)]
tsp_bb(matrix, n)
