import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
parent = [0] * (n+1)
result = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

prev = 0
for g in graph:
    cost, a, b = g

    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a != parent_b:
        prev = cost
        result += cost
        union_parent(parent, a, b)

result = result - prev

print(result)
        


