import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])


distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)