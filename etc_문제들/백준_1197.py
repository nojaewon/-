import sys
from heapq import heappop, heappush

heap = []
cost = 0

V, E = map(int, sys.stdin.readline().split())

visited = [False for _ in range(V+1)]
vertex = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().split())
    vertex[a].append((w, b))
    vertex[b].append((w, a))


visited[1] = True
for v in vertex[1]:
    heappush(heap, v)

while heap:
    target = heappop(heap)
    if visited[target[1]]:
        continue

    visited[target[1]] = True
    cost += target[0]

    for v in vertex[target[1]]:
        heappush(heap, v)

print(cost)
