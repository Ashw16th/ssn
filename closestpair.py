def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def brute_force(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

def closest_split_pair(px, py, delta, best_pair):
    mid_x = px[len(px) // 2][0]
    sy = [p for p in py if mid_x - delta <= p[0] <= mid_x + delta]
    best_dist = delta
    n = len(sy)
    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            d = distance(sy[i], sy[j])
            if d < best_dist:
                best_dist = d
                best_pair = (sy[i], sy[j])
    return best_pair, best_dist

def closest_pair_rec(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)
    
    mid = n // 2
    left_px, right_px = px[:mid], px[mid:]
    left_py, right_py = [], []

    for p in py:
        if p in left_px:
            left_py.append(p)
        else:
            right_py.append(p)

    left_pair, left_dist = closest_pair_rec(left_px, left_py)
    right_pair, right_dist = closest_pair_rec(right_px, right_py)

    if left_dist < right_dist:
        best_pair, delta = left_pair, left_dist
    else:
        best_pair, delta = right_pair, right_dist

    split_pair, split_dist = closest_split_pair(px, py, delta, best_pair)

    return (best_pair, delta) if delta < split_dist else (split_pair, split_dist)

def closest_pair(points):
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    pair, min_dist = closest_pair_rec(px, py)
    return pair, min_dist

points = []
n = int(input("Enter number of points: "))
for _ in range(n):
    x, y = map(int, input("Enter point (x y): ").split())
    points.append((x, y))

pair, min_dist = closest_pair(points)
print("Closest pair:", pair)
print("Minimum distance:", min_dist)
