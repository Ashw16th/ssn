class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def bound(u, n, capacity, items):
    if u.weight >= capacity:
        return 0
    profit_bound = u.value
    j = u.level + 1
    total_weight = u.weight

    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if j < n:
        profit_bound += (capacity - total_weight) * items[j].ratio

    return profit_bound

class Node:
    def __init__(self, level, value, weight):
        self.level = level
        self.value = value
        self.weight = weight

def knapsack_bb(n, items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    queue = []
    max_profit = 0
    queue.append(Node(-1, 0, 0))

    while queue:
        u = queue.pop(0)
        if u.level == n - 1:
            continue

        v = Node(u.level + 1, u.value + items[u.level + 1].value, u.weight + items[u.level + 1].weight)
        if v.weight <= capacity and v.value > max_profit:
            max_profit = v.value

        if bound(v, n, capacity, items) > max_profit:
            queue.append(v)

        v = Node(u.level + 1, u.value, u.weight)
        if bound(v, n, capacity, items) > max_profit:
            queue.append(v)

    print("\nMaximum Profit:", max_profit)

n = int(input("Enter number of items: "))
items = [Item(*map(int, input().split())) for _ in range(n)]
capacity = int(input("Enter knapsack capacity: "))

knapsack_bb(n, items, capacity)
