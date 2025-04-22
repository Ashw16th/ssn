class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def knapsack_approx(n, items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            break
    print("\nApproximate Maximum Profit:", total_value)

n = int(input("Enter number of items: "))
items = [Item(*map(int, input().split())) for _ in range(n)]
capacity = int(input("Enter knapsack capacity: "))

knapsack_approx(n, items, capacity)
